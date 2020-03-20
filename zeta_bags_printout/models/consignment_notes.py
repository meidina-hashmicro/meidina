# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ConsignmentNotes(models.Model):
    _name = 'consignment.notes'
    _description = 'Consignment Notes'
    _rec_name = 'nama'

    tgl_terima = fields.Date(string='Tgl Terima')
    nama = fields.Many2one(comodel_name='res.partner', string='Nama')
    alamat_tujuan_jika_retur = fields.Char(string='Alamat Tujuan Jika Retur')
    kota = fields.Char('Kota')
#     kota = fields.Selection(
#         string='Kota',
#         selection=[
#             ('ambon', 'Ambon'),
#             ('balikpapan', 'Balikpapan'),
#             ('banda_aceh', 'Banda Aceh'),
#             ('bandar_lampung', 'Bandar Lampung'),
#             ('bandung', 'Bandung'),
#             ('banjarbaru', 'Banjarbaru'),
#             ('banjarmasin', 'Banjarmasin'),
#             ('batam', 'Batam'),
#             ('batu', 'Batu'),
#             ('bau-Bau', 'Bau-Bau'),
#             ('bekasi', 'Bekasi'),
#             ('bengkulu', 'Bengkulu'),
#             ('bima', 'Bima'),
#             ('binjai', 'Binjai'),
#             ('bireuen', 'Bireuen'),
#             ('bitung', 'Bitung'),
#             ('blangkejeren', 'Blangkejeren'),
#             ('blitar', 'Blitar'),
#             ('bogor', 'Bogor'),
#             ('bontang', 'Bontang'),
#             ('bukittinggi', 'Bukittinggi'),
#             ('cianjur', 'Cianjur'),
#             ('cilegon', 'Cilegon'),
#             ('cimahi', 'Cimahi'),
#             ('cirebon', 'Cirebon'),
#             ('denpasar', 'Denpasar'),
#             ('depok', 'Depok'),
#             ('dumai', 'Dumai'),
#             ('gorontalo', 'Gorontalo'),
#             ('jakarta', 'Jakarta'),
#             ('jambi', 'Jambi'),
#             ('jayapura', 'Jayapura'),
#             ('kediri', 'Kediri'),
#             ('kendari', 'Kendari'),
#             ('kota_sorong', 'Kota Sorong'),
#             ('kupang', 'Kupang'),
#             ('langsa', 'Langsa'),
#             ('lhokseumawe', 'Lhokseumawe'),
#             ('lubuklinggau', 'Lubuklinggau'),
#             ('madiun', 'Madiun'),
#             ('magelang', 'Magelang'),
#             ('makassar', 'Makassar'),
#             ('malang', 'Malang'),
#             ('manado', 'Manado'),
#             ('manokwari', 'Manokwari'),
#             ('mataram', 'Mataram'),
#             ('medan', 'Medan'),
#             ('merauke', 'Merauke'),
#             ('metro', 'Metro'),
#             ('meulaboh', 'Meulaboh'),
#             ('mojokerto', 'Mojokerto'),
#             ('padang_panjang', 'Padang Panjang'),
#             ('padang_sidempuan', 'Padang Sidempuan'),
#             ('padang', 'Padang'),
#             ('pagar_alam', 'Pagar Alam'),
#             ('palangkaraya', 'Palangkaraya'),
#             ('palembang', 'Palembang'),
#             ('palopo', 'Palopo'),
#             ('palu', 'Palu'),
#             ('pangkal_pinang', 'Pangkal Pinang'),
#             ('pare_pare', 'Pare-Pare'),
#             ('pariaman', 'Pariaman'),
#             ('pasuruan', 'Pasuruan'),
#             ('payakumbuh', 'Payakumbuh'),
#             ('pekalongan', 'Pekalongan'),
#             ('pekanbaru', 'Pekanbaru'),
#             ('pematang_siantar', 'Pematang Siantar'),
#             ('pontianak', 'Pontianak'),
#             ('prabumulih', 'Prabumulih'),
#             ('probolinggo', 'Probolinggo'),
#             ('purwokerto', 'Purwokerto'),
#             ('redelong', 'Redelong (Simpang Tiga Redelong)'),
#             ('sabang', 'Sabang'),
#             ('salatiga', 'Salatiga'),
#             ('samarinda', 'Samarinda'),
#             ('sawah_lunto', 'Sawah Lunto'),
#             ('semarang', 'Semarang'),
#             ('serang', 'Serang'),
#             ('sibolga', 'Sibolga'),
#             ('sigli', 'Sigli'),
#             ('singkawang', 'Singkawang'),
#             ('singkil', 'Singkil'),
#             ('solok', 'Solok'),
#             ('south_tangerang', 'South Tangerang'),
#             ('sukabumi', 'Sukabumi'),
#             ('surabaya', 'Surabaya'),
#             ('surakarta', 'Surakarta'),
#             ('takengon', 'Takengon'),
#             ('tangerang', 'Tangerang'),
#             ('tanjung_balai', 'Tanjung Balai'),
#             ('tanjung_pinang', 'Tanjung Pinang'),
#             ('tapaktuan', 'Tapaktuan'),
#             ('tarakan', 'Tarakan'),
#             ('tasikmalaya', 'Tasikmalaya'),
#             ('tebing_tinggi', 'Tebing Tinggi'),
#             ('tegal', 'Tegal'),
#             ('tenggarong', 'Tenggarong'),
#             ('ternate', 'Ternate'),
#             ('tidore', 'Tidore'),
#             ('tomohon', 'Tomohon'),
#             ('tual', 'Tual'),
#             ('yogyakarta', 'Yogyakarta'),
#         ]
#     )
    kode_pos = fields.Char(string='Kode Pos')
    no_telp = fields.Char(string='No Telp')
    email = fields.Char(string='Email')
    no_rekening = fields.Char(string='No Rekening')
    a_n = fields.Char(string='a/n')
    bank = fields.Char(string='Bank')
    type = fields.Selection(
        string='Type',
        selection=[
            ('titp_jual', 'Titp Jual'),
            ('jual_lepas', 'Jual Lepas'),
        ]
    )
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.user.company_id)
    currency_id = fields.Many2one("res.currency", related='company_id.currency_id',
        string="Currency", readonly=True, required=True)
    ekspektasi_harga_anda = fields.Float(string='Ekspektasi Harga Anda')
    brand = fields.Char(string='Brand')
    category = fields.Many2one(comodel_name='product.category', related="model.categ_id", string='Category', store=True)
    model = fields.Many2one(comodel_name='product.product', string='Model')
    color = fields.Char(string='Color')
    year = fields.Char(string='Year')
    date_code = fields.Char(string='Date Code')
    size = fields.Char(string='Size')
    insole = fields.Char(string='Insole')
    original_receipt = fields.Boolean(string='Original Receipt(OR)')
    copy_receipt = fields.Boolean(string='Copy Receipt(CR)')
    authentication_card = fields.Boolean(string='Authentication Card(AC)')
    hologram_data_code = fields.Boolean(string='Hologram/Date Code(HG)')
    ribbon = fields.Boolean(string='Ribbon(RB)')
    camelia = fields.Boolean(string='Camelia(CM)')
    box = fields.Boolean(string='Box(BX)')
    paperbag = fields.Boolean(string='Paperbag(PB)')
    dustbag = fields.Boolean(string='Dustbag(DB)')
    small_dustbag = fields.Boolean(string='Small Dustbag(SD)')
    strap = fields.Boolean(string='Strap(ST)')
    controllato = fields.Boolean(string='Controllato(CO)')
    tags = fields.Boolean(string='Tags(TG)')
    booklet = fields.Boolean(string='Booklet(BC)')
    year_card = fields.Boolean(string='Year Card(YC)')
    padlock = fields.Boolean(string='Padlock(PL)')
    key = fields.Boolean(string='Key(KY)')
    clochette = fields.Boolean(string='Clochette(CH)')
    stopper = fields.Boolean(string='Stopper(SP)')
    raincoat = fields.Boolean(string='Raincoat(RC)')
    sample_leather = fields.Boolean(string='Sample Leather(SL)')
    cities = fields.Boolean(string='Cites(CT)')
    others = fields.Boolean(string='Others(OT)')
    others_text = fields.Char()
    
    note = fields.Text(string='Note')
    warehouse = fields.Many2one(comodel_name='stock.warehouse', string='Warehouse')
    whatsapp = fields.Char('Whatsapp')
    
    state = fields.Selection(
        string='Status',
        selection=[
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('received', 'Received'),
        ],
        default='draft',
    )

    picking_ids = fields.Many2many('stock.picking', compute='_compute_picking_ids', string='Picking associated to this sale')
    delivery_count = fields.Integer(string='Delivery Orders', compute='_compute_picking_ids')

    @api.multi
    def search_number(self):
        partners = self.env['res.partner'].search([('fax','=',self.whatsapp)])
        print "partners",partners
        if partners:
            for partner in partners:
                self.alamat_tujuan_jika_retur = partner.street
                self.kode_pos = partner.zip
                self.no_telp = partner.phone
                self.email = partner.email
                self.kota = partner.city
                self.nama = partner.id
        else:
            return {
                  'type': 'ir.actions.act_window', 
                  'view_type': 'form', 
                  'view_mode': 'form',
                  'res_model': 'warning.wizard', 
                  'target': 'new', 
                 }
        
    
    @api.onchange('nama')
    def partner_change(self):
        self.whatsapp = self.nama.fax
        self.alamat_tujuan_jika_retur = self.nama.street
        self.kode_pos = self.nama.zip
        self.no_telp = self.nama.phone
        self.email = self.nama.email
        self.kota = self.nama.city
    
    @api.multi
    def _compute_picking_ids(self):
        for consignment in self:
            consignment.picking_ids = self.env['stock.picking'].search([('consignment_notes_id', '=', consignment.id)]) or []
            consignment.delivery_count = len(consignment.picking_ids)

    @api.multi
    def action_view_delivery(self):
        action = self.env.ref('stock.action_picking_tree_all').read()[0]

        pickings = self.mapped('picking_ids')
        print pickings
#         if len(pickings) > 1:
        action['domain'] = ['|', ('id', 'in', pickings.ids), ('backorder_id','in',pickings.ids)]
#         elif pickings:
#             action['views'] = [(self.env.ref('stock.view_picking_form').id, 'form')]
#             action['res_id'] = pickings.id
        return action

    @api.multi
    def action_confirm_consignment_note(self):
        stock_env = self.env['stock.picking']
        if self.warehouse.out_type_id.default_location_dest_id:
            location_dest_id = self.warehouse.out_type_id.default_location_dest_id.id
        elif self.nama:
            location_dest_id = self.nama.property_stock_customer.id
        else:
            location_dest_id, supplierloc = self.env['stock.warehouse']._get_partner_locations()


        vals = {
            'consignment_notes_id': self.id,
            'partner_id': self.nama.id,
            'location_id': self.warehouse.id,
            'picking_type_id': self.warehouse.out_type_id.id,
            'location_dest_id': location_dest_id,
        }

        delivery_order = stock_env.create(vals)
        if self.model:
            move_line = {

                'product_id': self.model.id,
                'product_uom_qty': 1.0,
                'product_uom': self.model.uom_id.id,
                'location_id': self.warehouse.id,
                'location_dest_id': location_dest_id,
                'picking_type_id': self.warehouse.out_type_id.id,
                'name': 'This stock move line has been created by Consignment Note #' + str(self.id)
            }
            delivery_order.update({
                'move_lines': [(0, 0, move_line)]
            })
        print "delivery_order",delivery_order
        self.state="confirmed"
        return delivery_order

#     @api.multi
#     def action_reset_consignment_note(self):
#         if self.picking_ids:
#             for delivery in self.picking_ids:
#                 if delivery.state == 'draft':
#                     delivery.unlink()
#                 else:
#                     raise ValidationError(_('Can not delete picking as the stock is available!'))
#         self.state="draft"
