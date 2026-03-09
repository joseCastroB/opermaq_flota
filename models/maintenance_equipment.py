from odoo import models, api

class MaintenanceEquipment(models.Model):
    # Heredamos el modelo nativo de equipos de Odoo
    _inherit = 'maintenance.equipment'

    # Sobrescribimos la función que genera el nombre visual en todo el sistema
    @api.depends('name', 'model')
    def _compute_display_name(self):
        # 1. Dejamos que Odoo calcule el nombre estándar primero
        super()._compute_display_name()
        
        # 2. Recorremos cada equipo y le agregamos el modelo si es que lo tiene
        for equipment in self:
            if equipment.model:
                equipment.display_name = f"{equipment.display_name}/{equipment.model}"