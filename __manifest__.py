{
    'name': 'Student Management',
    'version': '15.1.0.0',
    'sequence': 185,
    'category': '',
    'website': 'https://www.odoo.com/app/fleet',
    'author': 'Sachitha Perera',
    'summary' : 'Manager Student Profiles',
    'description' : """""",
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequences.xml',
        'views/student_details_view.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
