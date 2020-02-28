from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class CreateCategoriaForm(FlaskForm):
   nombre = StringField(' Categoria:', validators=[DataRequired()])
   icono = StringField('Icono: ', validators=[DataRequired()])
   submit = SubmitField('Guardar')

class UpdateCategoriaForm(FlaskForm):
    nombre = StringField(' Categoria:', validators=[DataRequired()])
    icono = StringField('Icono: ', validators=[DataRequired()])
    submit = SubmitField('Actualizar')

