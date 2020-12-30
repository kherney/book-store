# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning


class Bookstore(models.Model):
    _name = 'bookstore.book'
    _description = "Books in Stock"
    book_name = fields.Char('Title', required=True)
    book_isbn = fields.Char('ISBN')
    book_active = fields.Boolean('Is Active', default=True)
    book_date_published = fields.Date()
    book_image = fields.Binary('Cover')
    book_publisher = fields.Many2one('res.partner', string="Publisher")
    book_ids_author = fields.Many2many('res.partner', string="Authors")

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
                raise Warning("Please provide a vañide ISBN tp {}".format(record.book_name))
        return True
