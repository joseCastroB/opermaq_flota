{
    'name': 'Flota Equipos',
    'version': '1.0',
    'category': 'Operations/Fleet',
    'summary': 'Control de flota, asignaciones y contratos de equipos',
    'description': """Módulo personalizado para la gestión integral de la flota de Opermaq.""",
    'author': 'Jose Castro - Tic Technologies',
    'depends': ['base', 'mail', 'maintenance', 'web_timeline', 'opermaq_mantenimiento'], # 'mail' es para poder tener el chat/historial en los registros
    'data': [
        'security/ir.model.access.csv',
        'views/contrato_flota_views.xml',
    ],
    'installable': True,
    'application': True, # ESTO ES VITAL: Le dice a Odoo que es una App principal, no un simple parche
    'license': 'LGPL-3',
}