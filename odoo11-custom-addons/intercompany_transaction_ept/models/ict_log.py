from openerp import models,fields,api, _
from openerp.exceptions import UserError, ValidationError
from datetime import datetime



class intercompany_log(models.Model):
    
    _name="ict.process.log.line"

    transfer_id = fields.Many2one("inter.company.transfer",string="Tansfer")

    message = fields.Char("Message")
    is_skiped = fields.Boolean("Skipped")
    