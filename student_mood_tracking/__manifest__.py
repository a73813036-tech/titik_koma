{
    'name': 'Student Mood Tracking',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Mencatat kondisi emosional harian mahasiswa',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/mood_tracking_views.xml',
    ],
    'installable': True,
    'application': True,
}