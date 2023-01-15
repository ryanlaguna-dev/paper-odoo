from odoo import fields, models, api, _
from odoo.tools.float_utils import float_is_zero, float_compare
from odoo.exceptions import UserError
import datetime


class MultipleBilled(models.TransientModel):

    _name = 'paper_soa.multiple_billed'


    @api.multi
    def toggle_billed_status(self):
        invoices = self.env['account.invoice'].browse(self._context.get('active_ids'))
        for invoice in invoices:
            invoice.write({"billed": not invoice.billed})
        return