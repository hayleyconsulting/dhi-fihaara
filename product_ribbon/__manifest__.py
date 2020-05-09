# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by 73lines
# See LICENSE file for full copyright and licensing details.
{
    'name': 'Website Ribbon',
    'summary': 'Product Ribbon',
    'description': 'Product Ribbon',
    'category': 'Website',
    'version': '13.0.0.2',
    'author': 'Vampy',
    'website': 'www.hayleyconsulting.com',
    'depends': ['website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/templates.xml',
        'views/product_ribbon_view.xml',
    ],
    'images': [
        'static/description/ecommerce_all_in_one_73lines.png',
    ],
    'installable': True,
    'auto_install': False,
    'currency': 'EUR',
}
