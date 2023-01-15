# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, api, fields, exceptions
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
import pdb


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.one
    @api.depends("partner_id")
    def _restrict_invoice(self):
        self.ensure_one()

        if self.partner_id:
            current_date = str(datetime.now().date())
            oldest_invoice = self.env["account.invoice"].search(
                [
                    ("state", "=", "open"),
                    ("date_due", "<", current_date),
                    ("partner_id", "=", self.partner_id.id),
                ],
                order="create_date desc",
            )
            if len(oldest_invoice) > 0 and oldest_invoice[0].date_due < current_date:
                self.restrict_invoice = True

            moveline_obj = self.env["account.move.line"]
            movelines = moveline_obj.search(
                [
                    ("partner_id", "=", self.partner_id.id),
                    ("account_id.user_type_id.name", "in", ["Receivable", "Payable"]),
                    ("full_reconcile_id", "=", False),
                ]
            )
            debit, credit = 0.0, 0.0
            today_dt = datetime.strftime(datetime.now().date(), DF)
            for line in movelines:
                if line.date_maturity < today_dt:
                    credit += line.debit
                    debit += line.credit

            if (
                (credit - debit + self.amount_total) > self.partner_id.credit_limit
            ) and not self.partner_id.over_credit:
                self.restrict_invoice = True

    @api.multi
    def _action_confirm(self):
        res = super(SaleOrder, self)._action_confirm()
        if not self.env.user.custom_admin and self.restrict_invoice:
            raise exceptions.ValidationError(
                "User is above credit limit, please contact Admin."
            )
        return res

    restrict_invoice = fields.Boolean("Restrict Invoice", compute=_restrict_invoice)


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    warehouse = fields.Boolean(string="Warehouse", default=False)
    lacking = fields.Boolean(string="Lacking", default=False)
    delivery_receipt_image = fields.Char(string="DR Image")
    delivery_receipt_image_file = fields.Binary(
        string="DR Image File", help="Manifest Image File"
    )
    manifest_image = fields.Char(string="Manifest Image")
    manifest_image_file = fields.Binary(
        string="Manifest Image File", help="Manifest Image File"
    )

    @api.onchange("lacking")
    def clear_dr_field(self):
        self.ensure_one()
        if self.lacking is False:
            self.write(
                {
                    "delivery_receipt_image": None,
                    "delivery_receipt_image_file": None,
                }
            )

    @api.model
    def create(self, vals):
        if vals.get("lacking") == True and not (
            vals.get("delivery_receipt_image")
            or vals.get("delivery_receipt_image_file")
        ):
            raise exceptions.ValidationError(
                "Delivery Receipt required if lacking is True."
            )
        return super(AccountInvoice, self).create(vals)
