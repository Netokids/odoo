from odoo import fields, models

class MultiAddAttendee(models.TransientModel):
    _name = 'multi.add.attendee.wizard'
    _description = "Multi Add Attendee"

    attendee_ids = fields.Many2many('res.partner', string="attendees")

    def add_attendee(self):
        attendee_obj = self.env['training.attendees']
        training_obj = self.env['training.module']
        context = dict(self._context)
        active_ids = context.get('active_ids')
        for training in training_obj.browse(active_ids):
            for attendee in self.attendee_ids:
                attendee_obj.create({
                    'attendee_id': attendee.id,
                    'training_id': training.id
                })