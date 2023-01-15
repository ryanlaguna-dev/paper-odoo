# -*- coding: utf-8 -*-
{
    "name": "ECV Hold Customer Limit",
    "summary": """
        Prevent creation of invoices for customers beyond their credit limit""",
    "description": """
        Prevent creation of invoices for customers beyond their credit limit
    """,
    "author": "Ryan Laguna",
    "website": "",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Custom",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "partner_credit_limit", "custom_admin"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
        "views/sale_report_templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
