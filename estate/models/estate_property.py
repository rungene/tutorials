# -*- coding: utf-8 -*-

from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = 'Estate Propery plans'

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Int()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Boolean()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')])
