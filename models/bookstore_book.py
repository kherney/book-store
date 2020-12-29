# -*- coding: utf-8 -*-

from odoo import models, fields


class Bookstore(models.Model):
    _name = 'bookstore.book'
    _description = "Books in Stock"
    book_name = fields.Char('Title', required=True)
    book_isbn = fields.Char('ISBN')
    book_active = fields.Boolean('Is Active')
    book_date_published = fields.Date()
    book_image = fields.Binary('Cover')
    book_publisher = fields.Many2one('res.partner', string="Publisher")
    book_ids_author = fields.Many2many('res.partner', string="Authors")
