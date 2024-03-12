# -*- coding: utf-8 -*-
# from odoo import http


# class OdooCopilot(http.Controller):
#     @http.route('/odoo__copilot/odoo__copilot', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo__copilot/odoo__copilot/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo__copilot.listing', {
#             'root': '/odoo__copilot/odoo__copilot',
#             'objects': http.request.env['odoo__copilot.odoo__copilot'].search([]),
#         })

#     @http.route('/odoo__copilot/odoo__copilot/objects/<model("odoo__copilot.odoo__copilot"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo__copilot.object', {
#             'object': obj
#         })
