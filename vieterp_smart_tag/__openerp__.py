# -*- coding: utf-8 -*-
# Free support at : info@vieterp.net
{
    'name': "VietERP Smart Tag",

    'summary': """
        Automatically add tag to customer/employee""",

    'description': """
1. Main features:
    - You can define rule to add a tag to any customer/employee

2. Why choose this?
    - Automatically add tag to customer

3. Settings:
    - Updating ...

4. Support:
    For any feedback, please send email to info@vieterp.net

    """,

    'author': "VietERP / Sang",
    'website': "http://www.vieterp.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Marketing',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'crm',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'data/cron.xml',
        'views/tag_partner_rule_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'images': [
        'static/description/icon.png'
    ],
    'installable': True,
    'application': True,
}
