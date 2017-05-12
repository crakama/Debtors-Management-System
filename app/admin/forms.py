# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class DeptorForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    fullname = StringField('Name', validators=[DataRequired()])
    mobileno = IntegerField('Mobile Number', validators=[DataRequired()])
    nationalid = IntegerField('ID Number', validators=[DataRequired()])
    deptamount = IntegerField('Amount', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
