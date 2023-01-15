# -*- coding: utf-8 -*-
from odoo import http

# class Bir(http.Controller):
#     @http.route('/bir/bir/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bir/bir/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bir.listing', {
#             'root': '/bir/bir',
#             'objects': http.request.env['bir.bir'].search([]),
#         })

#     @http.route('/bir/bir/objects/<model("bir.bir"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bir.object', {
#             'object': obj
#         })