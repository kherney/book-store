from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        user_admin = self.env.ref('base.user_admin')
        self.env = self.env(user=user_admin)
        self.Book = self.env['bookstore.book']
        self.book_test = self.Book.create({'book_name': '100 años de soledad',
                                           'book_isbn': '879-1-78439-279-6'})
        return result

    def test_create(self):
        self.assertEqual(self.book_test.book_active, True)

    def test_check_isbn(self):
       self.assertTrue(self.book_test._check_isbn)
