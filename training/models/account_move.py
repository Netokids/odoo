from  odoo import api, fields, models, _

class AccountMove(models.Model):
    _inherit = "account.move"

    description = fields.Char("Deskripsi")
    instagram = fields.Char("Instagram")
    twitter = fields.Char("Twitter") 