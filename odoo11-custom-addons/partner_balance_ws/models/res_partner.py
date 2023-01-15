# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class ResPartner(models.Model):
    
    _inherit = 'res.partner'
    
    partner_currency = fields.Many2one('res.currency',string="Partner Currency",compute='_get_partner_currency')
    balance_in_partner_currency = fields.Float(
        "Customer Balance",compute='_get_balance_in_partner_currency'
    )
    
    @api.multi
    def _get_partner_currency(self):
        for record in self:
            if record.property_product_pricelist:
                record.partner_currency = record.property_product_pricelist.currency_id
        
    @api.onchange('property_product_pricelist')
    def onchange_pricelist(self):
        if not self.ids:
            return
        self._get_partner_currency()
        self._get_balance_in_partner_currency()
        
        
    @api.multi
    def _get_balance_in_partner_currency(self):
        for record in self:
            if record.customer and not record.parent_id:
                partner_balance = record.debit - record.credit
                if record.partner_currency:
                    rate = record.currency_id._get_conversion_rate(record.currency_id,record.partner_currency)
                else:
                    rate = 1
                record.balance_in_partner_currency = rate * partner_balance
