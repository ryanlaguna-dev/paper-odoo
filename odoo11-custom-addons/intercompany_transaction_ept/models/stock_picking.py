from odoo import fields, api, models, _

class stock_picking(models.Model):
    _inherit = 'stock.picking'
    
    ict_id = fields.Many2one('inter.company.transfer',string="ICT",copy=False)

    @api.model
    def create(self,vals):
        picking  = super(stock_picking,self).create(vals)
        order_id = self.env['sale.order'].search([('name','=',picking.origin)])
        if not order_id:
            order_id = self.env['purchase.order'].search([('name','=',picking.origin)])
        if order_id and order_id.ict_id:
            picking.ict_id = order_id.ict_id.id
        return picking