# -*- coding: utf-8 -*-
{
    "name": "Custom Admin User",
    "summary": """
        Custom admin user for credit  limit and product sale""",
    "description": """
        Custom admin user for credit  limit and product sale
    """,
    "author": "Ryan Laguna",
    "website": "",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "admin",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "product", "sale", "partner_credit_limit"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
}
