# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    consignment_notes_id = fields.Many2one(
        comodel_name='consignment.notes',
        string='Consignment Notes',
        copy=False,
    )

    @api.multi
    def action_assign(self):
        # overridden method
        """ Check availability of picking moves.
        This has the effect of changing the state and reserve quants on available moves, and may
        also impact the state of the picking as it is computed based on move's states.
        @return: True
        """
        self.filtered(lambda picking: picking.state == 'draft').action_confirm()
        moves = self.mapped('move_lines').filtered(lambda move: move.state not in ('draft', 'cancel', 'done'))
        if not moves:
            raise UserError(_('Nothing to check the availability for.'))
        moves.action_assign()
        if self.consignment_notes_id and self.pack_operation_product_ids:
            lots = self.env['stock.pack.operation.lot'].search([('operation_id' ,'in', self.pack_operation_product_ids.ids)])
            lots.unlink()
            #commmented
            for pack_operation in self.pack_operation_product_ids:
                if pack_operation.product_id.master_product:
                    lot_name = self.consignment_notes_id.zeta_sequence_num
                else:
                    lot_name = self.consignment_notes_id.zeta_sequence_num+pack_operation.product_id.default_code
                lot_id = self.env['stock.production.lot'].search([('name','=', lot_name), ('product_id','=',pack_operation.product_id.id)])
                operation_lot = self.env['stock.pack.operation.lot'].create({'lot_name': lot_name,
                                                                             'lot_id': lot_id and lot_id.id or False,
                                                                             'operation_id': pack_operation.id})


#         if self.consignment_notes_id and self.state in ['assigned', 'done']:
#             self.consignment_notes_id.state = 'received'
        return True

    @api.multi
    def force_assign(self):
        # overridden method
        """ Changes state of picking to available if moves are confirmed or waiting.
        @return: True
        """
        self.mapped('move_lines').filtered(lambda move: move.state in ['confirmed', 'waiting']).force_assign()
#         if self.consignment_notes_id and self.state in ['assigned', 'done']:
#             self.consignment_notes_id.state = 'received'
        return True