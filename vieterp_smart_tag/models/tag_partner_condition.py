# -*- coding: utf-8 -*-
# Free support at : info@vieterp.net

from openerp import tools, models, fields, api

class vieterp_tag_partner_condition(models.Model):
    _name = 'tag.partner.condition'

    rule_id = fields.Many2one('tag.partner.rule', string='Rule')