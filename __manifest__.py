# -*- coding: utf-8 -*-
{
    'name': "bookstore",
    'summary': """ A library e-shop app based on odoo framework """,
    'description': """ A library e-shop app. """,
    'author': "Kevin Herney R.",
    'website': "",
    'category': 'Sales',
    'version': '13.0.0.2',
    'depends': ['base'],
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/bookstore_book.xml',
        'views/library_menu.xml',
        'views/book_list_template.xml',
        'reports/book_report.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
