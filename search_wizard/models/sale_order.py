from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def action_open_search_wizard(self):
        ctx = dict(self.env.context or {})
        ctx.update({
            "default_sale_order_id": self.id,
            "default_partner": self.partner_id.name,
        })

        action = {
            "name": ("Search Wizard"),
            "type": "ir.actions.act_window",
            "res_model": "sale.order.search",
            "view_mode": 'form',
            "target": "new",
            "context": ctx,
        }
        return action
