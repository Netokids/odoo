{
    'name' : 'training',
    'summary' : """odoo training""",
    'description' :  """Training module for managing trainings - training course""", 
    'author' : "My Company",
    'website' : "http://www.yourcompany.com",

    #categories can be used to filter modules in module 
    #check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    #for the full list

    'category' : 'test',
    'version' : '0.1',

    #any module necessary for this one to work correctly
    'depends' : ['base', 'account'],

    #always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'report/training_report.xml',
        'views/training.xml',
        'views/account_move_views.xml',
    ],
    #only loaded in demonstration mode
    'demo' : [
        'demo/xml',
    ],
}