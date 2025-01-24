from odoo import http
from odoo.http import request
import re
from collections import Counter
from PyPDF2 import PdfReader
import io

class PDFProcessorController(http.Controller):

    @http.route('/pdf_processor', type='http', auth='user', website=True)
    def index(self, **kwargs):
        return request.render('custom_module.index')

    @http.route('/pdf_processor/upload', type='http', auth='user', methods=['POST'], website=True, csrf=False)
    def upload_pdf(self, **kwargs):
        pdf_file = kwargs.get('pdf_file')
        if not pdf_file:
            return "No se adjuntó ningún archivo PDF.", 400

        try:
            pdf_bytes = io.BytesIO(pdf_file.read())
            reader = PdfReader(pdf_bytes)
            frecuencia = Counter()
            partes = {}

            for page_num, page in enumerate(reader.pages):
                texto = page.extract_text() or ""
                partes_pagina_dividida = texto.split("Kerf: ", 1)
                contenido_modificado = partes_pagina_dividida[1] if len(partes_pagina_dividida) > 1 else ""
                letras_con_dos_puntos = re.findall(r'[A-Z]{1,2}:', contenido_modificado)
                partes_pagina = [letra.rstrip(':') for letra in letras_con_dos_puntos] if letras_con_dos_puntos else re.findall(r'[A-Z]', contenido_modificado)
                dimensiones = re.findall(r'([A-Z]{1,2})\s+\d+\s+([\d,.]+)cm\s+([\d,.]+)cm', texto)
                letras_dimensiones = {dim[0]: (dim[1], dim[2]) for dim in dimensiones}

                partes[page_num + 1] = []
                for letra in partes_pagina:
                    altura, base = letras_dimensiones.get(letra, ("N/A", "N/A"))
                    partes[page_num + 1].append((letra, altura, base))
                    frecuencia[letra] += 1

            return request.render('custom_module.result', {
                'frecuencia_partes': frecuencia.items(),
                'partes': partes
            })

        except Exception as e:
            return f"Error procesando el archivo PDF: {str(e)}", 500