from odoo import fields, models, api


class SearchWizard(models.TransientModel):
    _name = 'sale.order.search'

    name = fields.Char(
        default='Recherche produit'
    )
    sale_order_id = fields.Many2one(
        comodel_name='sale.order',
    )
    partner = fields.Char(
        string='Reference interne'
    )
    product_name = fields.Char(
        string='Nom de produit'
    )
    price = fields.Float(
        string='Price'
    )
    category_id = fields.Many2one(
        comodel_name='product.category'
    )