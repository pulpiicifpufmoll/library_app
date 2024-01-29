# -*- coding: utf-8 -*-
{
    'name': "Gestion de biblioteca",
    'summary': "Gestión de biblioteca",
    'author': "David Acedo Pulpillo",
    'license': "AGPL-3",
    'website': "",
    'version': '1.0',
    'depends': ['base'],
    'application': True,
    'category': "Services/Library",

    "data": [
        "security/ir.model.access.csv",
        "security/library_security.xml",
        "views/book_view.xml",
        "views/book_list_template.xml"
        "views/library_menu.xml",
    ]
}
