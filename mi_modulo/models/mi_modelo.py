from odoo import models, fields, api

class MiModelo(models.Model):
    _inherit = "sale.order"

    campo_a_mostrar = fields.Char(string='Campo a mostrar')

    def mostrar_partes_seleccionadas(self):
        mensaje = self.campo_a_mostrar
        return {
            'type': 'ir.actions.act_window',
            'name': 'Mensaje',
            'view_mode': 'form',
            'res_model': 'mensaje.popup',
            'target': 'new',
            'context': {'default_mensaje': mensaje},
        }
