# -*- coding: utf-8 -*-

from odoo import api, fields, models


class WarningWizard(models.TransientModel):
    _name = "warning.wizard"
    
    name = fields.Char('Name')
    
    def create_customer(self):
        ctx = self._context.copy()
        ctx.update({'default_customer': True})
        return {
                  'type': 'ir.actions.act_window', 
                  'view_type': 'form', 
                  'view_mode': 'form',
                  'res_model': 'res.partner', 
                  'context': ctx
                  
                 }

