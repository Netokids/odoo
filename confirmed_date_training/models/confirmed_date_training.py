from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrderConfirmedDate(models.Model):
    _inherit = 'sale.order'
    
    confirmed_date = fields.Datetime(string='Confirmed Date')
    total_quantity = fields.Char(string='Total Quantity')

    def test_button(self):
        raise UserError('Test Button Clicked')
    
    def confirm_invoice(self):
        self.action_confirm()

    
    @api.model
    def action_confirm(self):
        res = super(SaleOrderConfirmedDate, self).action_confirm()
        # set the value of 'confirmed_date' to the current datetime
        self.confirmed_date = fields.Datetime.now()
        total_qty = 0
        for line in self.order_line:
            total_qty += line.product_uom_qty
        self.total_quantity = total_qty
        return res
    