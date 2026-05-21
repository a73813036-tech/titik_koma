from odoo import models, fields, api

class ChatbotAI(models.Model):
    _name = 'chatbot.ai'
    _description = 'Chatbot AI History'
    _order = 'tanggal desc'

    mahasiswa_id = fields.Many2one('res.users', string='Mahasiswa', default=lambda self: self.env.user, required=True)
    pesan_mahasiswa = fields.Text(string='Pesan Mahasiswa', required=True)
    respon_ai = fields.Text(string='Respon AI')
    tanggal = fields.Datetime(string='Tanggal', default=fields.Datetime.now)
