{
    'name': 'Konsultasi & Rujukan',
    'version': '1.0',
    'summary': 'Menangani rujukan konsultasi mahasiswa',
    'category': 'Education',
    'depends': ['base', 'konselor', 'self_assessment'],
    'data': [
        'security/ir.model.access.csv',
        'views/konsultasi_views.xml',
    ],
    'installable': True,
}
