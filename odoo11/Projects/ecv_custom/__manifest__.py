# -*- coding: utf-8 -*-
{
    "name": "ECV Custom modules",
    "summary": """
        Group of apps for ECV""",
    "description": """
        Group of apps for ECV that include custom inventory valuation 
    """,
    "author": "Ryan Laguna",
    "website": "",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Custom",
    "version": "0.1",
    "application": True,
    # any module necessary for this one to work correctly
    "depends": ["base", "sale", "stock", "web"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        "views/account_invoice.xml",
        "views/ecv_inventory.xml",
        "views/customer_tag.xml",
        "views/package_stickers.xml",
        "views/res_partner.xml",
        "views/sale_order.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
