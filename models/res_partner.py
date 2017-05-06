# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class res_partner_clinica(models.Model):
    _inherit = 'res.partner'
    
    data_nascimento = fields.Date('Data de nascimento')
    idade = fields.Integer('Idade', compute='_calc_data_nascimento')
    sexo = fields.Selection([('m','Masculino'),
                             ('f','Feminino')],
                            'Sexo')
    
    alergias = fields.Text('Alergias')
    obs = fields.Text('Observações')
    consultas_ids = fields.One2many('prontuario.consulta','paciente_id',
                                    string='Consultas')
    
    prontuarios_ids = fields.One2many('prontuario.prontuario', 'paciente_id',
                                      string='Prontuarios')
    
    count_consulta = fields.Integer('nro de Consultas', compute='count_consultas_e_pront')
    count_prontuario = fields.Integer('nro de prontuario', compute='count_consultas_e_pront')
    
    
    
    @api.one
    def count_consultas_e_pront(self):
        consultas = 0
        pront = 0
        for c in self.consultas_ids:
            consultas += 1
        for p in self.prontuarios_ids:
            pront += 1
        self.count_consulta = consultas
        self.count_prontuario = pront
        
    
    @api.multi
    def open_prontuario_action(self):
        action = self.env.ref('clinica_modulo.action_prontuario_tree_view')
        result = action.read()[0]
        result['domain'] = [('paciente_id', '=', self.ids)]
        return result
    
    @api.multi
    def open_consulta_action(self):
        action = self.env.ref('clinica_modulo.action_consulta_tree_view')
        result = action.read()[0]
        result['domain'] = [('paciente_id', '=', self.ids)]
        return result
    
    @api.one
    def _calc_data_nascimento(self):
        today = datetime.datetime.now()
        if self.data_nascimento:
            nasc = datetime.datetime.strptime(self.data_nascimento, "%Y-%m-%d").date()
            nova_idade = today.year - nasc.year
            self.idade = nova_idade
        else:
            self.idade = 0
        