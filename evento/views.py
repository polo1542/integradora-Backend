from flask import render_template, url_for, flash, request, redirect, Blueprint
from integradora.evento.forms import CreateEventoForm, UpdateEventoForm
from integradora.models import Evento, Categoria
from integradora import  db

evento = Blueprint('evento', __name__)

@evento.route('/crear_evento', methods=['GET', 'POST'])
def crear_evento():
    form = CreateEventoForm()
    form.categoria_id.choices=[(a.id, a.nombre) for a in Categoria.query.order_by(Categoria.nombre)]

    if request.method=='POST':
        evento = Evento(nombre=form.nombre.data, fecha=form.fecha.data, hora=form.hora.data, categoria_id=form.categoria_id.data)
        db.session.add(evento)
        db.session.commit()
        return redirect(url_for('evento.lista_evento'))

    return render_template('crear-evento.html', form=form)

@evento.route('/lista_eventos')
def lista_evento():
    eventos = Evento.query.all()
    return render_template('lista-evento.html', eventos=eventos)

@evento.route('/<int:id_evento>/update', methods=['GET', 'POST'])
def update_evento(id_evento):
    evento = Evento.query.get_or_404(id_evento)

    form = UpdateEventoForm()
    #form.categoria_id.choices=[(a.id, a.nombre) for a in Categoria.query.order_by(Categoria.nombre)]

    if form.validate_on_submit():
        evento.nombre = form.nombre.data
        evento.fecha = form.fecha.data
        evento.hora = form.hora.data
        #evento.categoria_id = form.categoria_id.data
        db.session.commit()
        return redirect(url_for('evento.lista_evento'))

    elif request.method == 'GET':
        form.nombre.data = evento.nombre
        form.fecha.data = evento.fecha
        form.hora.data = evento.hora
        #form.categoria_id.data = evento.categoria_id

    return render_template('editar-evento.html', form=form)

@evento.route('/<int:id_evento>/delete', methods=['GET','POST'])
def delete_evento(id_evento):

    evento = Evento.query.get_or_404(id_evento)

    db.session.delete(evento)
    db.session.commit()
    return redirect(url_for('evento.lista_evento'))