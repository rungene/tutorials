# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.tools import date_utils


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = 'Estate Propery plans'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        copy=False, default=date_utils.add(fields.Date.today(), months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(
        # string='Type',
        selection=[('north', 'North'), ('south', 'South'),
                   ('east', 'East'), ('west', 'West')])
    active = fields.Boolean(default=False)
    state = fields.Selection(
        selection=[
            ('new', 'New'), ('offer received', 'Offer Received'),
            ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'),
            ('cancelled', 'Cancelled')], default='new', copy=False,
            required=True
    )
