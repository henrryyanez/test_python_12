# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Library Management
        """,

    'description': """
        Practicas iniciales en el desarrollo de aplicaciones odoo
    """,

    'author': "Despliegue Digital",
    'website': "https://desplieguedigital.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    'installable':True,
}