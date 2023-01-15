# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date, datetime


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    billed = fields.Boolean(default=False, string="BILLED")
    delivered = fields.Boolean(string="Delivered", default=False)

    @api.multi
    @api.onchange("billed")
    def _billed_change(self):
        groups = self.env["res.groups"].search([("name", "=", "Billing")])

        if self.env.user.id not in groups.users.ids:
            raise UserError(_("Only manager level users can modify this field."))


class ResPartner(models.Model):

    _inherit = "res.partner"

    @api.multi
    def print_unbilled(self):
        return self.env.ref("paper_soa.action_print_soa").report_action(self)

    @api.multi
    def get_data(self):
        ids = [self.id]
        if self.is_company:
            for c in self.child_ids:
                ids.append(c.id)
        invoices = self.env["account.invoice"].search(
            [
                "&",
                "&",
                "&",
                ("partner_id", "in", ids),
                ("billed", "=", False),
                ("state", "=", "open"),
                ("delivered", "=", True),
            ]
        )
        return invoices

    @api.multi
    def get_current_date(self):
        return date.today().strftime("%m/%d/%Y")
