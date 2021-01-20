# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning, ValidationError


class Bookstore(models.Model):
    _name = 'bookstore.book'
    _description = "Books in Stock"
    _order = "book_name, book_date_published desc"
    _rec_name = "book_name"

    book_name = fields.Char('Title', required=True)
    book_isbn = fields.Char('ISBN')
    book_type = fields.Selection([('paper', 'Paperback'),
                                  ('hard', 'Hardcover'),
                                  ('electronic', 'Electronic'),
                                  ('other', 'Other')],
                                 "Type")
    book_notes = fields.Text("Internal Notes")
    book_desc = fields.Html("Descriptions")

    book_copies = fields.Integer(default=1)
    avg_rating = fields.Float("Average rating", digits=(3, 2))
    book_price = fields.Monetary('Price', 'currency_id')

    book_date_published = fields.Date()
    last_borrow_date = fields.Datetime("Last Borrow On",
                                       default=lambda self: fields.Datetime.now())

    book_active = fields.Boolean('Is Active', default=True)
    book_image = fields.Binary('Cover')

    currency_id = fields.Many2one(comodel_name='res.currency')
    book_publisher = fields.Many2one('res.partner', string="Publisher")
    book_author_ids = fields.Many2many('res.partner',
                                       string="Authors")
    book_publisher_country_related = fields.Many2one(comodel_name="res.country",
                                                     related="book_publisher.country_id",
                                                     readonly=True,
                                                     store=False,)
    book_publisher_city = fields.Char(string="Ciudad",
                                      related="book_publisher.city")
    book_publisher_country_id = fields.Many2one(comodel_name="res.country",
                                                string="Publisher Country",
                                                compute="_compute_publisher_country",
                                                inverse="_inverse_publisher_country",
                                                search="_search_publisher_country",
                                                store=False,)

    @api.depends("book_publisher.country_id")
    def _compute_publisher_country(self):
        for book in self:
            book.book_publisher_country_id = book.book_publisher.country_id

    def _inverse_publisher_country(self):
        for book in self:
            book.book_publisher.country_id = book.book_publisher_country_id

    def _search_publisher_country(self, operator, value):
        return [('book_publisher', operator, value)]

    @api.constrains('book_isbn')
    def _constrain_isbn_valid(self):
        for book in self:
            if book.book_isbn and not book._check_isbn():
                raise ValidationError("{} no is a valide ISBN value".format(book.book_isbn))

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.book_isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def check_isbn_button(self):
        for record in self:
            if not record.book_isbn:
                raise Warning("Please provide a ISBN to {}".format(record.book_name))
            elif record.book_isbn and not self._check_isbn():
                raise Warning("Please provide a valide ISBN tp {}".format(record.book_name))
        return True
