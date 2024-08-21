from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_open_wizard(self):
        context = dict(self.env.context)
        context.update({
            'default_client': self.partner_id.name,
            'default_order_id': self.id,
        })
        action = {
            'name': ("wizard"),
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.wizard',
            'context': context,
            'view_mode': 'form',
            'target': 'new',
        }
        return action