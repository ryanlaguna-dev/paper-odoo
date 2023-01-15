# -*- coding: utf-8 -*-
{
    'name': 'Partner Balance',
    'version': '1.0',
    'category': 'Tools',
    'author':'WEBSuite Solutions',
    'maintainer': 'WEBSuite Solutions',
    'summary': 'Check for your customer balance in partner view',
    'license': 'LGPL-3',
    'support':'websuite.solutions@gmail.com',
    'sequence': 1,
    'depends': [
        'sale'
    ],
    'data': [
       'views/res_partner.xml'
    ],
    'css': ['static/src/css/description.css'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/main_screen.png'],
    'price': 10.00,
    'currency': 'EUR',
}
