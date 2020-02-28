from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired

class CreateRegistradoForm(FlaskForm):
    nombre = StringField('Registrado:', validators=[DataRequired()])
    apellido = StringField('Apellido: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    fecha = StringField('Fecha: ', validators=[DataRequired()])
    pases = StringField('Pases: ', validators=[DataRequired()])
    talleres = StringField('Talleres: ', validators=[DataRequired()])
    total = StringField('Total: ', validators=[DataRequired()])
    regalo_id = IntegerField('Id de Regalo', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class UpdateRegistradoForm(FlaskForm):
    nombre = StringField('Registrado:', validators=[DataRequired()])
    apellido = StringField('Apellido: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    fecha = StringField('Fecha: ', validators=[DataRequired()])
    pases = StringField('Pases: ', validators=[DataRequired()])
    talleres = StringField('Talleres: ', validators=[DataRequired()])
    total = StringField('Total: ', validators=[DataRequired()])
    regalo_id = IntegerField('Id de Regalo', validators=[DataRequired()])
    submit = SubmitField('Actualizar')