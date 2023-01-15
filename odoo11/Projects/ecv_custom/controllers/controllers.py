# -*- coding: utf-8 -*-
from odoo import http

# class EcvCustom(http.Controller):
#     @http.route('/ecv_custom/ecv_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ecv_custom/ecv_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ecv_custom.listing', {
#             'root': '/ecv_custom/ecv_custom',
#             'objects': http.request.env['ecv_custom.ecv_custom'].search([]),
#         })

#     @http.route('/ecv_custom/ecv_custom/objects/<model("ecv_custom.ecv_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ecv_custom.object', {
#             'object': obj
#         })