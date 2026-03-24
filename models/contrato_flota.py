from odoo import models, fields, api

class OpermaqContratoFlota(models.Model):
    _name = 'opermaq.contrato.flota'
    _description = 'Contrato de Flota de Equipos'
    # Heredamos mail para tener el historial de notas y mensajes al fondo del formulario
    _inherit = ['mail.thread', 'mail.activity.mixin'] 

    name = fields.Char(string='Referencia de Contrato', required=True, copy=False, default='Nuevo')
    
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True, tracking=True)
    
    # Aquí aplicamos el DOMAIN para que solo traiga equipos Propios
    # Nota: Si tu campo opermaq_estado_equipo_id es un Selection, el domain sería: [('opermaq_estado_equipo_id', '=', 'propio')]
    equipment_id = fields.Many2one(
        'maintenance.equipment', 
        string='Equipo', 
        required=True,
        domain="[('opermaq_estado_equipo_id.name', 'ilike', 'Propio')]", 
        tracking=True
    )
    
    maquina = fields.Char(related='equipment_id.maquina', string='Máquina')
    marca = fields.Char(related='equipment_id.marca', string='Marca')
    modelo = fields.Char(related='equipment_id.model', string='Modelo')
    serie = fields.Char(related='equipment_id.serial_no', string='Serie')
    medida_ruedas = fields.Char(related='equipment_id.medida_ruedas', string='Medida de Ruedas')

    fecha_inicio = fields.Datetime(string='Fecha Inicio', required=True, tracking=True)
    fecha_fin = fields.Datetime(string='Fecha Fin', required=True, tracking=True)

    nro_oc_contrato = fields.Char(string='Nro. OC / Contrato', tracking=True)

    almacen = fields.Char(string='Almacén', tracking=True)

    # Autogenerador de código de contrato al darle a Guardar
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Nuevo') == 'Nuevo':
                # Genera algo como: CONTRATO - 202603091530
                vals['name'] = "CONTRATO - " + str(fields.Datetime.now().strftime('%Y%m%d%H%M'))
        return super(OpermaqContratoFlota, self).create(vals_list)