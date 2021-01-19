from odoo import models, fields


class Bookstore(models.Model):
    _name = "bookstore.book.category"
    _description = "Books category"
    _parent_store = True

    name = fields.Char(translate=True, required=True)
    parent_id = fields.Many2one(comodel_name="bookstore.book.category",
                                string="Parent Category",
                                ondelete="restrict")
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many(comodel_name="bookstore.book.category",
                                inverse_name="parent_id",
                                string="Subcategories")
    highlighted_ids = fields.Reference([('bookstore.book', 'Book'),
                                        ('res.partner', 'Author'), ],
                                       string=" Category Highlight")
