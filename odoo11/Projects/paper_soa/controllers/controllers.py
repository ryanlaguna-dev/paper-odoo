# -*- coding: utf-8 -*-
from odoo import http

# class Paper-soa(http.Controller):
#     @http.route('/paper-soa/paper-soa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/paper-soa/paper-soa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('paper-soa.listing', {
#             'root': '/paper-soa/paper-soa',
#             'objects': http.request.env['paper-soa.paper-soa'].search([]),
#         })

#     @http.route('/paper-soa/paper-soa/objects/<model("paper-soa.paper-soa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('paper-soa.object', {
#             'object': obj
#         })