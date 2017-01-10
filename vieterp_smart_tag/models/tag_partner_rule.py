# -*- coding: utf-8 -*-
# Free support at : info@vieterp.net

from openerp import tools, models, fields, api

class vieterp_tag_partner_rule(models.Model):
    _name = 'tag.partner.rule'

    tag_id = fields.Many2one('res.partner.category', string='Tag')
    condition_ids = fields.One2many('tag.partner.condition', 'rule_id', string='Conditions')

    @api.multi
    def compute_tag(self):
        return True