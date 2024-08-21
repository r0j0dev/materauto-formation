# -*- coding: utf-8 -*-
# from odoo import http


# class OmContextwizard(http.Controller):
#     @http.route('/om_contextwizard/om_contextwizard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_contextwizard/om_contextwizard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_contextwizard.listing', {
#             'root': '/om_contextwizard/om_contextwizard',
#             'objects': http.request.env['om_contextwizard.om_contextwizard'].search([]),
#         })

#     @http.route('/om_contextwizard/om_contextwizard/objects/<model("om_contextwizard.om_contextwizard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_contextwizard.object', {
#             'object': obj
#         })
