from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class CreateEventoForm(FlaskForm):
    nombre = StringField('Evento:', validators=[DataRequired()])
    fecha = StringField('Fecha Evento: ', validators=[DataRequired()])
    hora = StringField('Hora: ', validators=[DataRequired()])
    submit = SubmitField('Guardar')

