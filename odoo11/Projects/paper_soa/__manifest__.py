# -*- coding: utf-8 -*-
{
    "name": "Custom Statement of Account",
    "summary": """
        ECV Paper statement of account module.""",
    "description": """
        ECV Paper statement of account module.
    """,
    "author": "Ryan Laguna",
    "website": "",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Report",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "account",
        "account_pdc",
    ],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
        "report/statement_report.xml",
        "report/deposit_slip.xml",
        "wizard/multiple_billed_toggle.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
