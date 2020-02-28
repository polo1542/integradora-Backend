from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class CreateRegaloForm(FlaskForm):
    nombre = StringField('Regalo:', validators=[DataRequired()])
   
    submit = SubmitField('Guardar')

class UpdateRegaloForm(FlaskForm):
    nombre = StringField('Regalo:', validators=[DataRequired()])
    submit = SubmitField('Actualizar')