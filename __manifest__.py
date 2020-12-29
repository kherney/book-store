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
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/bookstore_book.xml',
        'views/library_menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
