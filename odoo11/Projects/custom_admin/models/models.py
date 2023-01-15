# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Users(models.Model):
    _inherit = "res.users"
    custom_admin = fields.Boolean(string="Custom Admin", default=False)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def write(self, vals):
        if "standard_price" in vals:
            if vals["standard_price"] > self.standard_price:
                vals["sale_ok"] = False

        return super(ProductTemplate, self).write(vals)

    @api.onchange("sale_ok")
    def restrict_sale_ok(self):
        if not self.env.user.custom_admin:
            raise UserError(_("Only custom admins can update can be sold status."))

    @api.depends("qty_available")
    def restrict_sale(self):
        if self.qty_available < 1:
            self.write({"sale_ok": False})


class ProductProduct(models.Model):
    _inherit = "product.product"

    def write(self, vals):
        if "standard_price" in vals:
            if vals["standard_price"] > self.standard_price:
                product_template = self.env["product.template"].search(
                    [("id", "=", self.product_tmpl_id.id)]
                )
                product_template.write({"sale_ok": False})

        return super(ProductProduct, self).write(vals)

    @api.depends("qty_available")
    def restrict_sale(self):
        if self.qty_available < 1:
            template = self.env["product.template"].search(
                [("id", "=", self.product_tmpl_id.id)]
            )
            template.write({"sale_ok": False})


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.onchange("customer")
    def restrict_customer_status(self):
        if not self.env.user.custom_admin:
            raise UserError(
                _("Only custom admins can update Is a Customer status."),
            )


class SupplierInfo(models.Model):
    _inherit = "product.supplierinfo"

    @api.multi
    def write(self, vals):
        if "price" in vals:
            if vals.get("price") > self.price:
                template = self.env["product.template"].search(
                    [("id", "=", self.product_tmpl_id.id)]
                )
                template.write({"sale_ok": False})

        return super(SupplierInfo, self).write(vals)


# class StockMove(models.Model):
#     _inherit = "stock.move"

#     @api.one
#     @api.depends("product_id", "product_uom", "product_uom_qty")
#     def _restrict_sale(self):
#         if self.product_qty < 1:
#             template = self.env["product.template"].search(
#                 [("id", "-", self.product_tmpl_id.id)]
#             )
#             template.write({"sale_ok": False})
