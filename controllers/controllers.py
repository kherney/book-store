# -*- coding: utf-8 -*-
# from odoo import http


# class Bookstore(http.Controller):
#     @http.route('/bookstore/bookstore/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bookstore/bookstore/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bookstore.listing', {
#             'root': '/bookstore/bookstore',
#             'objects': http.request.env['bookstore.bookstore'].search([]),
#         })

#     @http.route('/bookstore/bookstore/objects/<model("bookstore.bookstore"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bookstore.object', {
#             'object': obj
#         })
