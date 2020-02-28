from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

class CreateInvitadoForm(FlaskForm):
    nombre = StringField('Invitado:', validators=[DataRequired()])
    apellido = StringField('Apellido: ', validators=[DataRequired()])
    descripcion = StringField('Descripcion: ', validators=[DataRequired()])
    imagen = FileField('Imagen: ', validators=[FileAllowed(['jpg','png','jpeg'])])
    evento_id = IntegerField('Id de Evento', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class UpdateInvitadoForm(FlaskForm):
    nombre = StringField('Invitado:', validators=[DataRequired()])
    apellido = StringField('Apellido: ', validators=[DataRequired()])
    descripcion = StringField('Descripcion: ', validators=[DataRequired()])
    imagen = FileField('Imagen: ', validators=[FileAllowed(['jpg','png','jpeg'])])
    #evento_id = IntegerField('Id de Evento', validators=[DataRequired()])
    submit = SubmitField('Actualizar')