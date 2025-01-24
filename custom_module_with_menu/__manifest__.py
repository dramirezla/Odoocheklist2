{
    'name': 'PDF Processor',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Procesa un archivo PDF y muestra botones interactivos',
    'description': 'Este módulo permite cargar un archivo PDF, extraer datos y mostrar partes como botones interactivos.',
    'author': 'David Alejandro Ramírez',
    'depends': ['web'],
    'data': [
        'views/pdf_processor_menu.xml',
        'views/pdf_processor_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_module/static/src/css/styles.css',
            'custom_module/static/src/js/script.js',
        ],
    },
    'installable': True,
    'application': True,
}