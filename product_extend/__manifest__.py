# -*- coding: utf-8 -*-
{
    'name': "Product",

    'summary': """
        Herencia en el modulo product
        agregando un campo seleccionable Tipologia
        """,

    'description': """
        Herencia en el modulo product
        agregando un campo seleccionable Tipologia
    """,

    'author': "Despliegue Digital",
    'website': "https://desplieguedigital.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'views/product_view.xml',
    ],
    'installable':True,
    'application':True,
}