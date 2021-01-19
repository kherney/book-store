from odoo import models, fields


class Bookstore(models.Model):
    _inherit = "res.partner"

    publisher_books_ids = fields.One2many(comodel_name="bookstore.book",
                                          inverse_name="book_publisher",
                                          string="Book publishers")
    books_ids = fields.Many2many(comodel_name="bookstore.book",
                                 string="Books")
