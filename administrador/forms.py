from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

class CreateAdministradorForm(FlaskForm):
   imagen = FileField('Imagen: ', validators=[FileAllowed(['jpg','png','jpeg'])])
    email = StringField('Apellido: ', validators=[DataRequired()])
    username = StringField('Descripcion: ', validators=[DataRequired()])
    password_hash = StringField('Descripcion: ', validators=[DataRequired()])
    
    
    submit = SubmitField('Guardar')

class UpdateAdministradorForm(FlaskForm):
    imagen = FileField('Imagen: ', validators=[FileAllowed(['jpg','png','jpeg'])])
    email = StringField('Email: ', validators=[DataRequired()])
    username = StringField('Nombre: ', validators=[DataRequired()])
    password_hash = StringField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Actualizar')