# -*- coding: utf-8 -*-

from odoo import models, fields, api


class account_payment(models.Model):
    _inherit = "account.payment"

    bir_reported = fields.Boolean(
        string="BIR Reported",
        default=False,
    )


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    bir_reported = fields.Boolean(
        string="BIR Reported",
        default=False,
    )
