from odoo import models, fields, api

class MiModelo(models.Model):
    _inherit = "sale.order"
    _name = 'mi.modelo'
    _description = 'Descripción de mi modelo'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha = fields.Date(string='Fecha')

    def mostrar_partes_seleccionadas(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'name': 'Hola mundo'
        }
