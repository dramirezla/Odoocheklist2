from odoo import models, fields

class MensajePopup(models.TransientModel):
  _name = 'mensaje.popup'

  mensaje = fields.Text(string="Mensaje")
