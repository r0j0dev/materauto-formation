from odoo import fields, models, api

class SaleOrderWizard(models.TransientModel):
    _name = 'sale.order.wizard'

    name = fields.Char(
        default='Wizard'
    )

    client = fields.Char()
    order_id = fields.Many2one(
        comodel_name='sale.order'
    )

    def print_context(self):
        print(self.env.context)
    
