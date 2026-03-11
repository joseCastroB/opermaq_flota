from odoo import models, fields, tools

class ReporteEstadoFlota(models.Model):
    _name = 'opermaq.reporte.estado.flota'
    _description = 'Reporte de Disponibilidad de Flota'
    # ¡EL TRUCO! _auto=False evita que Odoo cree una tabla normal, en su lugar usaremos SQL
    _auto = False

    equipment_id = fields.Many2one('maintenance.equipment', string='Equipo', readonly=True)
    estado = fields.Selection([
        ('alquilado', 'Alquilado (Con Contrato)'),
        ('stand_by', 'Stand By (Disponible)')
    ], string='Estado Actual', readonly=True)

    def init(self):
        # Eliminamos la vista anterior para que Odoo la construya de nuevo con el filtro
        tools.drop_view_if_exists(self.env.cr, self._table)
        
        # Inyectamos el nuevo código SQL
        self.env.cr.execute(f"""
            CREATE OR REPLACE VIEW {self._table} AS (
                SELECT
                    e.id as id,
                    e.id as equipment_id,
                    CASE
                        WHEN EXISTS (
                            SELECT 1 FROM opermaq_contrato_flota c
                            WHERE c.equipment_id = e.id
                              AND c.fecha_inicio <= (NOW() AT TIME ZONE 'UTC')
                              AND c.fecha_fin >= (NOW() AT TIME ZONE 'UTC')
                        ) THEN 'alquilado'
                        ELSE 'stand_by'
                    END as estado
                FROM maintenance_equipment e
                JOIN opermaq_estado_equipo est ON e.opermaq_estado_equipo_id = est.id
                WHERE est.name ILIKE '%Propio%'
            )
        """)