from odoo import models, fields, api

class Konselor(models.Model):
    _name = 'pendamping.konselor'
    _description = 'Data Tenaga Konselor/Psikolog'

    # Relasi ke Admin yang mengelola data ini (sesuai ERD)
    # Di Odoo, admin biasanya merujuk ke res.users
    admin_id = fields.Many2one('res.users', string='Admin Pengelola', default=lambda self: self.env.user)

    # Atribut sesuai Class Diagram & ERD
    nama = fields.Char(string='Nama Konselor', required=True)
    spesialis = fields.Char(string='Spesialisasi') # Dari ERD 
    nomor_wa = fields.Char(string='Nomor WhatsApp')
    jadwal = fields.Text(string='Jadwal Praktik')
    link_wa = fields.Char(string='Link WhatsApp Otomatis', compute='_compute_link_wa', store=True)

    # Method untuk menghasilkan link WA secara otomatis (Logic dapatkan_link_wa)
    @api.depends('nomor_wa')
    def _compute_link_wa(self):
        for rec in self:
            if rec.nomor_wa:
                # Membersihkan nomor dari karakter non-angka
                clean_phone = ''.join(filter(str.isdigit, rec.nomor_wa))
                # Format internasional (asumsi Indonesia +62)
                if clean_phone.startswith('0'):
                    clean_phone = '62' + clean_phone[1:]
                rec.link_wa = f"https://wa.me/{clean_phone}"
            else:
                rec.link_wa = False

    # Method tampilkan_profil() bisa dihandle oleh view Form di Odoo