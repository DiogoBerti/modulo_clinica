# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Prontuario(models.Model):
    _name = 'prontuario.prontuario'
    
    paciente_id = fields.Many2one('res.partner', string='Paciente')
    
    observacoes_medicas = fields.Text(u'Observações médicas')
    diagnostico = fields.Text(u'Diagnóstico')
    data_nascimento = fields.Date('Data de Nascimento',
                                   related='paciente_id.data_nascimento')
    idade_paciente = fields.Integer('Idade', related='paciente_id.idade')
    
    medico_id = fields.Many2one('res.users', u'Médico responsável')
    

class ProntuarioConsulta(models.Model):
    _name = 'prontuario.consulta'
    
    data_consulta = fields.Datetime('Data da Consulta', required=True)
    
    tipo_consulta = fields.Selection([('periodico','Periodico'),
                                       ('retorno','Retorno'),
                                       ('emergencia','Emergencia')],
                                       'Tipo da Consulta')
    
    paciente_id = fields.Many2one('res.partner', string='Paciente')
    
    prontuario_id = fields.Many2one('prontuario.prontuario', string='Paciente')
    
    local_consulta = fields.Selection([('sede','Sede'),
                                       ('unidade','Unidade')],
                                      'Local da consulta')
    
    
        
    
    