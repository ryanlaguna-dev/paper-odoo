# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResConfigSettings(models.TransientModel):
	_inherit = 'res.config.settings'

	is_digital_sign = fields.Boolean(String="Allow Digital Signature in Sale Order")
	is_confirm_sign_sale = fields.Boolean("Required Signature on Sale Order Confirmation")

	@api.model
	def get_values(self):
		res = super(ResConfigSettings, self).get_values()
		res.update(
			is_digital_sign=(self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_digital_sign')),
			is_confirm_sign_sale=(self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_confirm_sign_sale'))
		)
		return res

	@api.multi
	def set_values(self):
		super(ResConfigSettings, self).set_values()
		self.env['ir.config_parameter'].sudo().set_param('digital_signature.is_digital_sign',self.is_digital_sign),
		self.env['ir.config_parameter'].sudo().set_param('digital_signature.is_confirm_sign_sale',self.is_confirm_sign_sale),

class SaleOrder(models.Model):
	_inherit = "sale.order"

	@api.model
	def _digital_sign_sale_order(self):
		is_digital_sign = (self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_digital_sign'))
		return is_digital_sign

	@api.model
	def _confirmation_sign_sale(self):
		is_confirm_sign_sale = (self.env['ir.config_parameter'].sudo().get_param('digital_signature.is_confirm_sign_sale'))
		return is_confirm_sign_sale

	@api.multi
	def action_confirm(self):
		res=super(SaleOrder,self).action_confirm()
		if self.confirmation_sign_sale_compute:
			if self.digital_signature:
				res=super(SaleOrder,self).action_confirm()
			else:
				raise UserError(_('Please add "Digital Signature" for confirm sale order...!'))
		else:
			res = super(SaleOrder,self).action_confirm()
		return res

	digital_signature = fields.Binary(string="Digital Signature")
	digital_sign_sale_order_compute = fields.Text(default=_digital_sign_sale_order)
	confirmation_sign_sale_compute = fields.Text(default=_confirmation_sign_sale)
