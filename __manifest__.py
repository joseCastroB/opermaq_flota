{
    'name': 'Flota Equipos',
    'version': '1.0',
    'category': 'Operations/Fleet',
    'summary': 'Control de flota, asignaciones y contratos de equipos',
    'description': """
        Módulo personalizado para la gestión integral de la flota de Opermaq.
        Incluye:
        - Control de equipos y vehículos.
        - Gestión de contratos.
        - Asignaciones.
    """,
    'author': 'Opermaq',
    'depends': ['base', 'mail'], # 'mail' es para poder tener el chat/historial en los registros
    'data': [
        # Aquí iremos agregando nuestros archivos XML y permisos más adelante:
        # 'security/ir.model.access.csv',
        # 'views/menu_views.xml',
    ],
    'installable': True,
    'application': True, # ESTO ES VITAL: Le dice a Odoo que es una App principal, no un simple parche
    'license': 'LGPL-3',
}