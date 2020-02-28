from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired

class CreateEventoForm(FlaskForm):
    nombre = StringField('Evento:', validators=[DataRequired()])
    fecha = StringField('Fecha Evento: ', validators=[DataRequired()])
    hora = StringField('Hora: ', validators=[DataRequired()])
    categoria_id = SelectField('Selecciona Categoria', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class UpdateEventoForm(FlaskForm):
    nombre = StringField('Evento:', validators=[DataRequired()])
    fecha = StringField('Fecha Evento: ', validators=[DataRequired()])
    hora = StringField('Hora: ', validators=[DataRequired()])
    #categoria_id = SelectField('Selecciona Categoria', validators=[DataRequired()])
    submit = SubmitField('Actualizar')