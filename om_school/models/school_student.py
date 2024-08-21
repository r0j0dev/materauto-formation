from odoo import fields, models, api
from datetime import date

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Students of school'

    name = fields.Char(string="Nom")
    image = fields.Image(string="Photo")
    age = fields.Integer(
        string="Age",
        compute= "_compute_age"
    )

    genre = fields.Selection([
        ('femel', "Feminin"),
        ('male', "Masculin"),
        ], string="Genre",
    )

    datenaissance = fields.Datetime(
        string="Date de naissance",
    )

    groupesanguin = fields.Selection([
        ('grpA', "A"),
        ('grpB', "B"),
        ], string="Groupe sanguin",
    )

    nationalite = fields.Many2one(
        comodel_name='res.country.state',
        string='Nationalite',
        required=False)

    @api.depends('datenaissance')
    def _compute_age(self):

        for record in self:
            yearcurr = date.today().year
            if record.nationalite:
                agestud = record.datenaissance.year
                record.age = yearcurr - agestud
            else:
                record.age = 0



