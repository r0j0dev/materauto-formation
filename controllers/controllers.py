# -*- coding: utf-8 -*-
# from odoo import http


# class Reptel-mto(http.Controller):
#     @http.route('/reptel-mto/reptel-mto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reptel-mto/reptel-mto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reptel-mto.listing', {
#             'root': '/reptel-mto/reptel-mto',
#             'objects': http.request.env['reptel-mto.reptel-mto'].search([]),
#         })

#     @http.route('/reptel-mto/reptel-mto/objects/<model("reptel-mto.reptel-mto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reptel-mto.object', {
#             'object': obj
#         })
