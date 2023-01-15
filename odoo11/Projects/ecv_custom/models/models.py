# -*- coding: utf-8 -*-
from io import BytesIO
import base64

from odoo import models, fields, api, _
from odoo.exceptions import UserError, AccessError, ValidationError

import qrcode


class StockQuant(models.Model):
    _inherit = "stock.quant"

    standard_cost = fields.Float(
        string="Standard Price", related="product_tmpl_id.standard_price"
    )
    total_cost = fields.Float(compute="_compute_total_on_hand")

    @api.one
    @api.depends("standard_cost", "quantity")
    def _compute_total_on_hand(self):
        self.total_cost = self.standard_cost * self.quantity


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_customer_tags(self):
        query = self.env["ecv_custom.customer_tag"].search([])
        tags = []
        tag_query = [(tag.slug, tag.name) for tag in query]
        tags += tag_query
        return tags

    total_qty_undelivered = fields.Float(
        compute="_compute_total_undelivered_qty", string="Total Quantity Undelivered"
    )
    customer_tag = fields.Selection(
        _get_customer_tags, string="Customer Tag", required=True
    )
    package_count = fields.Integer(string="No. of Packages", default=0)
    dr_number = fields.Char(string="DR Number")
    manifest_image = fields.Char(string="Manifest Image")
    manifest_image_file = fields.Binary(
        string="Manifest Image File", help="Manifest Image File"
    )


    @api.multi
    def print_stickers(self):
        """
        Print stickers for all invoices for this manifest
        """
        self.ensure_one()
        if self.package_count < 1:
            ValidationError("Package count less than 1.")
        return self.env.ref("ecv_custom.sticker_printing").report_action(self)

    @api.one
    @api.depends("order_line")
    def _compute_total_undelivered_qty(self):
        total = 0
        for line in self.order_line:
            total += line.product_uom_qty - line.qty_invoiced
        return total

    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        self.ensure_one()
        journal_id = self.env["account.invoice"].default_get(["journal_id"])[
            "journal_id"
        ]

        if not journal_id:
            raise UserError(
                _("Please define an accounting sales journal for this company.")
            )

        invoice_vals = {
            "name": self.client_order_ref or "",
            "origin": self.name,
            "type": "out_invoice",
            "account_id": self.partner_invoice_id.property_account_receivable_id.id,
            "partner_id": self.partner_invoice_id.id,
            "partner_shipping_id": self.partner_shipping_id.id,
            "journal_id": journal_id,
            "currency_id": self.pricelist_id.currency_id.id,
            "comment": self.note,
            "payment_term_id": self.payment_term_id.id,
            "fiscal_position_id": self.fiscal_position_id.id
            or self.partner_invoice_id.property_account_position_id.id,
            "company_id": self.company_id.id,
            "user_id": self.user_id and self.user_id.id,
            "team_id": self.team_id.id,
            "customer_tag": self.customer_tag,
            "manifest_image": self.manifest_image,
            "manifest_image_file": self.manifest_image_file,
        }
        return invoice_vals

    @api.onchange("partner_id")
    def _change_customer_tag(self):
        if self.partner_id.customer_tag:
            self.customer_tag = self.partner_id.customer_tag

    # @api.multi
    # def _generate_and_get_qr_code(self):
    #     self.ensure_one()
    #     local = f"http://localhost:8069/web#id={self.id}&view_type=form&model=sale.order&menu_id=176&action=245"

    #     prod = f"http://192.168.0.102:8069/web#id={self.id}&view_type=form&model=sale.order&menu_id=176&action=245"

    #     img = qrcode.make(local)
    #     img_loc = f"qr_{self.name}"
    #     img.save(img_loc)
    #     return img_loc

    @api.multi
    def generate_qr(self):
        url = self.env["ir.config_parameter"].get_param("web.base.url")
        url += f"/web#id={str(self.id)}&view_type=form&model=sale.order"
        qr_code = qrcode.QRCode(version=4, box_size=4, border=1)
        qr_code.add_data(url)
        qr_code.make(fit=True)
        qr_img = qr_code.make_image()
        im = qr_img._img.convert("RGB")
        buffered = BytesIO()
        im.save(buffered, format="png")
        img_str = base64.b64encode(buffered.getvalue()).decode("ascii")
        return img_str


class CustomerTag(models.Model):
    _name = "ecv_custom.customer_tag"
    _description = "Customer Tag"
    _inherit = ["mail.thread", "mail.activity.mixin", "portal.mixin"]

    name = fields.Char(
        string="Tag Name",
        required=True,
    )
    slug = fields.Char(string="Slug")

    _sql_constraints = [
        ("unique_tag", "unique(name)", "Customer tag already exists."),
    ]

    @api.model
    def create(self, vals):

        vals["slug"] = "_".join(vals["name"].replace("-", "").split()).lower()
        tag = super(CustomerTag, self).create(vals)
        return tag


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def _get_customer_tags(self):
        query = self.env["ecv_custom.customer_tag"].search([])
        tags = []
        tag_query = [(tag.slug, tag.name) for tag in query]
        tags += tag_query
        return tags

    customer_tag = fields.Selection(
        _get_customer_tags, string="Customer Tag", required=True
    )

    @api.onchange("partner_id")
    def _change_customer_tag(self):
        if self.partner_id.customer_tag:
            self.customer_tag = self.partner_id.customer_tag


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _get_customer_tags(self):
        query = self.env["ecv_custom.customer_tag"].search([])
        tags = []
        tag_query = [(tag.slug, tag.name) for tag in query]
        tags += tag_query
        return tags

    customer_tag = fields.Selection(
        _get_customer_tags, string="Customer Tag", required=True
    )
