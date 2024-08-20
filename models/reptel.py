from odoo import models, fields


class reptel(models.Model):
    _name = 'reptel'

    employee_id = fields.Many2one('hr.employee')
    name = fields.Char(related='employee_id.name', string="Nom")
    numero = fields.Char(related='employee_id.mobile_phone', string="Numéro téléphone")
    departement_id = fields.Many2one('hr.department', string="Département")