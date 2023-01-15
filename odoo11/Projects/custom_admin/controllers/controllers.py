# -*- coding: utf-8 -*-
from odoo import http

# class CustomAdmin(http.Controller):
#     @http.route('/custom_admin/custom_admin/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_admin/custom_admin/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_admin.listing', {
#             'root': '/custom_admin/custom_admin',
#             'objects': http.request.env['custom_admin.custom_admin'].search([]),
#         })

#     @http.route('/custom_admin/custom_admin/objects/<model("custom_admin.custom_admin"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_admin.object', {
#             'object': obj
#         })