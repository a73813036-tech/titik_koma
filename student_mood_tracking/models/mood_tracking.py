from odoo import models, fields, api

class StudentMoodTracking(models.Model):
    _name = 'student.mood.tracking'
    _description = 'Student Daily Mood Tracking'
    _order = 'date desc'

    student_id = fields.Many2one('res.users', string='Mahasiswa', default=lambda self: self.env.user, required=True)
    date = fields.Date(string='Tanggal', default=fields.Date.context_today, required=True)
    
    mood_level = fields.Selection([
        ('1', 'Sangat Sedih / Tertekan'),
        ('2', 'Sedih / Lelah'),
        ('3', 'Biasa Saja'),
        ('4', 'Senang / Bersemangat'),
        ('5', 'Sangat Bahagia')
    ], string='Kondisi Emosi', required=True)
    
    note = fields.Text(string='Catatan Tambahan')
    
    # Menghitung warna untuk representasi visual di dashboard/kanban
    color = fields.Integer(compute='_compute_color')

    @api.depends('mood_level')
    def _compute_color(self):
        for record in self:
            colors = {'1': 1, '2': 2, '3': 4, '4': 3, '5': 10}
            record.color = colors.get(record.mood_level, 0)