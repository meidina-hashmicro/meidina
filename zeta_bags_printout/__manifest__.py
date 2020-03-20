# -*- coding: utf-8 -*-
{
    'name': "Zeta Bags Printout",

    'summary': """Consignment Notes Module""",

    'description': """
        Long description of Consignment Notes Module's purpose
    """,

    'author': "Hashmicro | Krushndevsinh Jadeja",
    'website': "https://www.hashmicro.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '10.0.1.0.2',
    'sequence': '1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/report_paperformat.xml',
        'wizard/warning_wizard_view.xml',
        'views/consignment_notes_views.xml',
        'views/stock_picking_views.xml',
        'reports/report_consignment_note_views.xml',
        'reports/report_layout.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}