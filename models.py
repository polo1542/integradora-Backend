from integradora import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class Evento(db.Model):

    __tablename__ = 'eventos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    fecha = db.Column(db.String(64), nullable=False)
    hora = db.Column(db.String(64), nullable=False)
    categoria_id =db.Column(db.Integer, db.ForeignKey('categorias.id'))
    invitados = db.relationship('Invitado', backref="evento", lazy='dynamic')
    
    def __init__(self, nombre, fecha, hora, categoria_id):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.categoria_id = categoria_id

    def __repr__(self):
        return f"Nombre: { self.nombre }"

    def report_invitados(self):
        print('Aqui estan los invitados a este evento')
        for invitado in self.invitados:
            print(invitado.nombre)

class Invitado(db.Model):

    __tablename__ = 'invitados'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    apellido = db.Column(db.String(64), nullable=False)
    descripcion = db.Column(db.String(128), nullable=True)
    imagen = db.Column(db.String(128), nullable=False, default="imagen.png")
    evento_id = db.Column(db.Integer, db.ForeignKey('eventos.id'))
        
    def __init__(self, nombre, apellido, descripcion, evento_id):
        self.nombre = nombre
        self.apellido = apellido
        self.descripcion = descripcion
        self.evento_id = evento_id
    
    def __repr__(self):
        return f"Nombre_invitado: { self.nombre }"

class Categoria(db.Model):

    __tablename__ = 'categorias'
        
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    icono = db.Column(db.String(64), nullable=False)
    eventos = db.relationship('Evento', backref='categoria',lazy='dynamic')
            
    def __init__(self, nombre, icono):
        self.nombre = nombre
        self.icono = icono
        
    def __repr__(self):
        return f"Categoria: { self.nombre }"

    def report_eventos(self):
        print('Estos son los eventos que pernenecen a esta categoria')
        for evento in self.eventos:
            print(evento.nombre)
    
class Registrado(db.Model):

    __tablename__ = 'registrados'
            
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    apellido = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    fecha = db.Column(db.String(64), nullable=False)
    pases = db.Column(db.String(128), nullable=False)
    talleres = db.Column(db.String(64), nullable=False)
    total = db.Column(db.String(128), nullable=False)
    regalo_id = db.Column(db.Integer, db.ForeignKey('regalos.id'))
                
    def __init__(self, nombre, apellido, email, fecha, pases, talleres, total, regalo_id):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.fecha = fecha
        self.pases = pases
        self.talleres = talleres
        self.total = total
        self.regalo_id = regalo_id
            
    def __repr__(self):
        return f"Registrado: { self.nombre }"
        
class Regalo(db.Model):

    __tablename__ = 'regalos'
        
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    registrados = db.relationship('Registrado', backref='regalo', lazy='dynamic')
            
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __repr__(self):
        return f"Regalo: { self.nombre }"

    def report_registrados(self):
        print('Este regalo lo tienen estos registrados')
        for registrado in registrados:
            print(registrado.nombre)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f"Username { self.username }"