from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    note_field = StringField('Add New Note', validators=[DataRequired()])
    add = SubmitField('Add')

class DeleteForm(FlaskForm):
    id_field = StringField('Delete Note by ID', validators=[DataRequired()])
    delete = SubmitField('Delete')