{
    'name' : 'Perpustakaan',
    'summary' : """odoo training""",
    'description' :  """Training module for managing library""", 
    'author' : "Dion Novalino",
    'website' : "http://www.yourcompany.com",

    #categories can be used to filter modules in module 
    #check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    #for the full list

    'category' : 'perpustakaan',
    'version' : '0.1',

    #any module necessary for this one to work correctly
    'depends' : ['base','product'],

    #always loaded
    'data': [
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'views/perpustakaan.xml',
    ],
    #only loaded in demonstration mode
    'demo' : [
        'demo/xml',
    ],
}