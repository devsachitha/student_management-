from odoo import api, fields, models, _


class StudentDetails(models.Model):
    _name = "student.details"
    _description = "Manage Student Details"

    name = fields.Char(string="Full Name", required=True)
    age = fields.Integer(string="Age", required=True)


