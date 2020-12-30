# -*- coding: utf-8 -*-
from odoo import http


class Bookstore(http.Controller):

    @http.route('/library/books', auth='user')
    def list_books(self, **kwargs):
        books_rqst = http.request.env['bookstore.book']
        books = books_rqst.search([])
        return http.request.render(
            'bookstore.book_list_template', {'book_recordset': books}
        )
