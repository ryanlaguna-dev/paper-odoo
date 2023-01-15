# -*- coding: utf-8 -*-
from odoo import http

# class DeliveryReportTemplate(http.Controller):
#     @http.route('/delivery_report_template/delivery_report_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delivery_report_template/delivery_report_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delivery_report_template.listing', {
#             'root': '/delivery_report_template/delivery_report_template',
#             'objects': http.request.env['delivery_report_template.delivery_report_template'].search([]),
#         })

#     @http.route('/delivery_report_template/delivery_report_template/objects/<model("delivery_report_template.delivery_report_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delivery_report_template.object', {
#             'object': obj
#         })