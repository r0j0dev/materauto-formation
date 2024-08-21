# -*- coding: utf-8 -*-
# from odoo import http


# class ContextWizard(http.Controller):
#     @http.route('/context_wizard/context_wizard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/context_wizard/context_wizard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('context_wizard.listing', {
#             'root': '/context_wizard/context_wizard',
#             'objects': http.request.env['context_wizard.context_wizard'].search([]),
#         })

#     @http.route('/context_wizard/context_wizard/objects/<model("context_wizard.context_wizard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('context_wizard.object', {
#             'object': obj
#         })
