from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class PemimjamanBuku(models.Model):
    _name='peminjaman.buku'
    _description="Pinjam Buku"

    def _get_date(self):
        return fields.Date.today()

    def _get_date_kembali(self):
        return fields.Date.today() + relativedelta(days=7)
    
    def _get_number(self):
        return self.env['ir.sequence'].next_by_code('perpustakaan.sequence')

    name = fields.Char(string="Nomer", default=_get_number)
    tanggal_pinjam = fields.Date(string="Tanggal Pinjam", default=_get_date)
    tanggal_kembali=fields.Date(string="Tanggal Kembali")
    peminjam_id = fields.Many2one('res.partner', string='Peminjam')
    no_telpon = fields.Char(string="No Telpon")
    petugas_id = fields.Many2one('res.users', string='Petugas')
    daftar_buku_ids = fields.One2many('daftar.buku', 'peminjaman_id', string='Daftar Buku')
    total_harga_pinjam = fields.Float(string='Total Harga Pinjam' , compute='_compute_total_harga_pinjam', store=True)
    status = fields.Selection([('dipinjamkan', 'Dipinjamkan'), ('dikembalikan', 'Dikembalikan')], string="Status", default='dipinjamkan')
    status_pembayaran = fields.Char(string="Status Pembayaran", readonly=True, store=True, default='belum_lunas')
    

    @api.onchange('tanggal_pinjam')
    def _onchange_tanggal_pinjam(self):
        if self.tanggal_pinjam:
            self.tanggal_kembali = self.tanggal_pinjam + relativedelta(days=7)

    @api.depends('daftar_buku_ids')
    def _compute_total_harga_pinjam(self):
        for rec in self:
            rec.total_harga_pinjam = sum([line.harga_pinjam_buku for line in rec.daftar_buku_ids])
    
            
class DaftarBuku(models.Model):
    _name="daftar.buku"
    _description="Daftar Buku"

    buku_id = fields.Many2one('product.product',string='Buku')
    peminjaman_id = fields.Many2one('peminjaman.buku', string='Nomor Peminjaman')
    harga_pinjam_buku = fields.Float(string='Harga Pinjam Buku', readonly=False, store=True, force_save='1', compute='_compute_harga_pinjam_buku')

    @api.depends('buku_id')
    def _compute_harga_pinjam_buku(self):
        for rec in self:
            rec.harga_pinjam_buku = rec.buku_id.list_price

class ProductProduct(models.Model):
    _inherit = 'product.product'

    sinopsis = fields.Text(string='Sinopsis')
    tanggal_pinjam = fields.Date(string='Tanggal Pinjam')
    tanggal_kembali=fields.Date(string="Tanggal Kembali")
    peminjam_id = fields.Many2one('res.partner', string='Peminjam')
    no_telpon = fields.Char(string="No Telpon")
    petugas_id = fields.Many2one('res.users', string='Petugas')
    daftar_buku_ids = fields.One2many('daftar.buku', 'buku_id', string='Daftar Buku')
    total_harga_pinjam = fields.Float(string='Total Harga Pinjam')
    status = fields.Selection([('dipinjamkan', 'Dipinjamkan'), ('dikembalikan', 'Dikembalikan')], string="Status", default='dipinjamkan')

