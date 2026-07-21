# -*- coding: utf-8 -*-

from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = 'Estate Propery Types'

    name = fields.Char(required=True)
