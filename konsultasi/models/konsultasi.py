from odoo import models, fields, api

class Konsultasi(models.Model):
    _name = 'konsultasi.rujukan'
    _description = 'Rujukan Konsultasi'

    mahasiswa_id = fields.Many2one('res.users', string='Mahasiswa', default=lambda self: self.env.user, required=True)
    konselor_id = fields.Many2one('pendamping.konselor', string='Konselor', required=True)
    assessment_id = fields.Many2one('self.assessment', string='Assessment Terkait')
    tanggal_konsultasi = fields.Date(string='Tanggal Konsultasi', default=fields.Date.context_today)
    catatan = fields.Text(string='Catatan Rujukan')
