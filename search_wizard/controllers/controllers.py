# -*- coding: utf-8 -*-
# from odoo import http


# class SearchWizard(http.Controller):
#     @http.route('/search_wizard/search_wizard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/search_wizard/search_wizard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('search_wizard.listing', {
#             'root': '/search_wizard/search_wizard',
#             'objects': http.request.env['search_wizard.search_wizard'].search([]),
#         })

#     @http.route('/search_wizard/search_wizard/objects/<model("search_wizard.search_wizard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('search_wizard.object', {
#             'object': obj
#         })
