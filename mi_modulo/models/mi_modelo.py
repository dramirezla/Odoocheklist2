from odoo import models, fields, api

class MiModelo(models.Model):
    _inherit = "sale.order"

    def mostrar_partes_seleccionadas(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'name': 'Hola mundo'
        }
