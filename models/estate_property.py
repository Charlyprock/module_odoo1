from odoo import models, fields

class estatePropertyModel(models.Model):
    _name = "estate.estate_property"
    _description = """ Un model pour les propriété de mes imobiliers."""
    name = fields.Char()