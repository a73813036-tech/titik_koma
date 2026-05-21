from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    jenis_kelamin = fields.Selection([
        ('pria', 'Laki-laki'),
        ('wanita', 'Perempuan')
    ], string='Jenis Kelamin')
    
    instansi = fields.Char(string='Instansi/Universitas')
    no_telepon = fields.Char(string='Nomor Telepon')
    tanggal_daftar = fields.Date(string='Tanggal Daftar', default=fields.Date.context_today)
