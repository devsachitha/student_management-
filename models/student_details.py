from odoo import api, fields, models, _
from odoo.exceptions import UserError


class StudentDetails(models.Model):
    _name = "student.details"
    _description = "Manage Student Details"

    registration_number = fields.Char(string="Reg ID", readonly=1)
    first_name = fields.Char(string="First Name", required=1)
    last_name = fields.Char(string="Last Name")
    name = fields.Char(string="Full Name", readonly=1)
    age = fields.Integer(string="Age")

    @api.model
    def create(self, values):
        """Override Default create method -  Calling When create a new record"""
        # reg_id = self.env['ir.sequence'].next_by_code('student.reg')
        # values['registration_number'] = reg_id
        values['registration_number'] = self.env['ir.sequence'].next_by_code('student.reg')

        # first_name = values['first_name']
        # last_name = values['last_name']
        # age = values['age']
        # full_name = first_name + ' ' + last_name + ' ' + str(age)
        # values['name'] = full_name
        if 'last_name' in values:
            # Last name not equal to False
            if values['last_name']:
                values['name'] = values['first_name'] + ' ' + values['last_name'] + ' ' + str(values['age'])
            else:
                # Pop Up user error
                raise UserError("Please enter Last name")
        # Code modification
        # super create method
        # values pass into create method
        return super(StudentDetails, self).create(values)

    def write(self, values):
        """Overrider default write method  -  calling when edit the record """
        # check first name or last name available in values
        if 'first_name' in values and 'last_name' in values:
            values['name'] = values['first_name'] + ' ' + values['last_name']
        elif 'first_name' in values:
            # last_name = self.last_name
            values['name'] = values['first_name'] + ' ' + self.last_name
        elif 'last_name' in values:
            values['name'] = self.first_name + ' ' + values['last_name']
        return super(StudentDetails, self).write(values)
