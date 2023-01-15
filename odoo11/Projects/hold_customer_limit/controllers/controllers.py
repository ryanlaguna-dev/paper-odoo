# -*- coding: utf-8 -*-
from odoo import http

# class HoldCustomerLimit(http.Controller):
#     @http.route('/hold_customer_limit/hold_customer_limit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hold_customer_limit/hold_customer_limit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hold_customer_limit.listing', {
#             'root': '/hold_customer_limit/hold_customer_limit',
#             'objects': http.request.env['hold_customer_limit.hold_customer_limit'].search([]),
#         })

#     @http.route('/hold_customer_limit/hold_customer_limit/objects/<model("hold_customer_limit.hold_customer_limit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hold_customer_limit.object', {
#             'object': obj
#         })