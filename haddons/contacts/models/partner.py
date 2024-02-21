from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    cni = fields.Char(string='CNI')
    niu = fields.Char(string='NUI')

    @api.depends('type')
    def _inverse_cni_niu(self):
        for partner in self:
            if partner.type == 'individual':
                if partner.cni and len(partner.cni) != 11:
                    raise ValidationError('Le CNI doit avoir 11 caractères')
            elif partner.type == 'company':
                if partner.niu and len(partner.niu) != 14:
                    raise ValidationError('Le NUI doit avoir 14 caractères')
