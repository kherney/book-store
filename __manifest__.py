# -*- coding: utf-8 -*-
{
    'name': "bookstore",
    'summary': """ A library e-shop app based on odoo framework """,
    'description': """ A library e-shop app. """,
    'author': "Kevin Herney R.",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
