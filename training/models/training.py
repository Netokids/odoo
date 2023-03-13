from odoo.exceptions import ValidationError
from odoo import models, fields, api

class TrainingCourse(models.Model):
    _name = 'training.module'
    _description ='Training Course'

    def _get_date(self):
        return fields.Date.today()
    
    def _get_number(self):
        return self.env['ir.sequence'].next_by_code('training.sequence')

    name = fields.Char(string='name')
    registration_amount = fields.Float(string='Registration Amount ')
    date = fields.Date(string='Training Date', default=_get_date)
    description = fields.Text(string='description')
    state = fields.Selection([('draft', 'Draft'), ('inprogress', 'In progress'), ('done','Done')], string="Status", default='draft')
    attendee_ids = fields.One2many('training.attendees', 'training_id', string='Attendees')
    total_attendees = fields.Integer(string='Total Attendees',compute='_compute_total', store=True)
    total_attendees_presence = fields.Integer(string='Total Attendees Presence', compute='_compute_total_presence')
    trainer_id = fields.Many2one('res.users', string='Trainer')
    phone = fields.Char(string="Phone")
    training_number=fields.Char(string='Number', readonly=True, copy=False, default=_get_number)

    _sql_constraints=[
        ('training_unique', 'UNIQUE(name)', 'A name must be unique!')
    ]

    @api.constrains('registration_amount')
    def _check_registration_amount(self):
        if self.registration_amount <= 0:
            raise ValidationError('Registration amount must be greater than zero')
        
    @api.depends('attendee_ids')
    def _compute_total(self):
        for item in self: 
            item.total_attendees = len(item.attendee_ids)

    @api.depends('attendee_ids.presence')
    def _compute_total_presence(self):
        for item in self:
            attendees = item.attendee_ids.filtered(lambda a: a.presence)
            item.total_attendees_presence = len(attendees)
    
    def _compute_traning(self):
        training_obj = self.env['training.module']
        training = training_obj.search([('trainer_id', '=', self.id)])
        self.training_ids = training.ids 

    @api.onchange('trainer_id')
    def _onchange_trainer_id(self):
        if self.trainer_id:
            self.phone = self.trainer_id.phone
    

class TrainingAttendees(models.Model):
    _name='training.attendees'
    _description= 'Training Attendees'
    attendee_id = fields.Many2one('res.partner', string="Attendee")
    presence = fields.Boolean(string="presence")
    training_id = fields.Many2one('training.module', string='Training')    
    assistant_ids = fields.Many2many('res.users', string='Assistant')


class ResUsers(models.Model): 
    _inherit = 'res.users'
    training_ids=fields.Many2many('training.module', string='Training')






