# -*- coding: utf-8 -*-
{
    "name": "BIR Module",
    "summary": """
        BIR Related features""",
    "description": """
        BIR Related features
    """,
    "author": "Ryan Laguna",
    "website": "",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Custom Module",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "sale", "account"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
}
