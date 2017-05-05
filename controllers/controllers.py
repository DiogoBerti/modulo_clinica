# -*- coding: utf-8 -*-
from odoo import http

# class ClinicaModulo(http.Controller):
#     @http.route('/clinica_modulo/clinica_modulo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clinica_modulo/clinica_modulo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clinica_modulo.listing', {
#             'root': '/clinica_modulo/clinica_modulo',
#             'objects': http.request.env['clinica_modulo.clinica_modulo'].search([]),
#         })

#     @http.route('/clinica_modulo/clinica_modulo/objects/<model("clinica_modulo.clinica_modulo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clinica_modulo.object', {
#             'object': obj
#         })