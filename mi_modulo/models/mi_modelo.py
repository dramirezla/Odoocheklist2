from odoo import models, fields, api

class MiModelo(models.Model):
    _inherit = "sale.order"

    campo_a_mostrar = fields.Text(string='Campo a mostrar')

    def mostrar_partes_seleccionadas(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': campo_a_mostrar
            }
        }
