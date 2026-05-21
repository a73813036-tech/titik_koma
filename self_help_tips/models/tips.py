from odoo import models, fields, api

class SelfHelpTips(models.Model):
    _name = 'self_help.tips'
    _description = 'Konten Bantuan Mandiri'

    judul = fields.Char(string='Judul Tips', required=True)
    admin_id = fields.Many2one('res.users', string='Admin Pengelola', default=lambda self: self.env.user)
    isi_tips = fields.Html(string='Isi Tips/Artikel', required=True)
    
    level_resiko = fields.Selection([
        ('rendah', 'Resiko Rendah (Sehat/Stress Ringan)'),
        ('sedang', 'Resiko Sedang (Cemas/Sedih)'),
        ('tinggi', 'Resiko Tinggi (Butuh Bantuan Segera)')
    ], string='Level Resiko Terkait', required=True)

    tanggal_publikasi = fields.Date(string='Tanggal Publikasi', default=fields.Date.context_today)
