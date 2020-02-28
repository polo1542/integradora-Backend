from flask import render_template, request, Blueprint
from integradora.models import Categoria, Evento, Invitado,Regalo
#from webpersonal.models import Project

core = Blueprint('core',__name__)

@core.route('/')
def index():
   categorias = Categoria.query.all()
   eventos = Evento.query.all()
   invitados = Invitado.query.all()
   return render_template('index.html', categorias=categorias, eventos=eventos, invitados=invitados)
 

@core.route('/calendario')
def calendario():
   eventos = Evento.query.all()
   return render_template('calendario.html', eventos=eventos)

@core.route('/conferencia')
def conferencia():
    return render_template('conferencia.html')

@core.route('/invitados')
def invitados():
    invitados = Invitado.query.all()
    return render_template('invitados.html', invitados=invitados)

@core.route('/reservaciones')
def reservaciones():
    regalos = Regalo.query.all()
    eventos = Evento.query.all()
    return render_template('reservaciones.html', regalos=regalos, eventos=eventos)



#@core.route('/evento/crear_evento')
#def evento():
    #return render_template('crear-evento.html')



#@core.route('/login')
#def login():
    #return render_template('login.html')

