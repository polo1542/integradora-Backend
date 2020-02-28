from flask import render_template, url_for, flash, request, redirect, Blueprint
from integradora.evento.forms import CreateRegistradoForm, UpdateRegistradoForm
from integradora.models import Registrado
from integradora import  db

registrado = Blueprint('registrado', __name__)

@registrado.route('/crear_registrado', methods=['GET', 'POST'])
def crear_registrado():
    form = CreateRegistradoForm()

    if form.validate_on_submit():
        registrado = Registrado(nombre=form.nombre.data, apellido=form.apellido.data, email=form.email.data,fecha=form.fecha.data, pases=form.pases.data,talleres=form.talleres.data,total=form.total.data, regalo_id=form.regalo_id.data)
        db.session.add(registrado)
        db.session.commit()
        return redirect(url_for('registrado.lista_registrado'))

    return render_template('crear-evento.html', form=form)

@evento.route('/lista_eventos')
def lista_evento():
    eventos = Evento.query.all()
    return render_template('lista-evento.html', eventos=eventos)

@evento.route('/<int:id_evento>/update', methods=['GET', 'POST'])
def update_evento(id_evento):
    evento = Evento.query.get_or_404(id_evento)

    form = UpdateEventoForm()

    if form.validate_on_submit():
        evento.nombre = form.nombre.data
        evento.fecha = form.fecha.data
        evento.hora = form.hora.data
        db.session.commit()
        return redirect(url_for('evento.lista_evento'))

    elif request.method == 'GET':
        form.nombre.data = evento.nombre
        form.fecha.data = evento.fecha
        form.hora.data = evento.hora

    return render_template('editar-evento.html', form=form)

@evento.route('/<int:id_evento>/delete', methods=['GET','POST'])
def delete_evento(id_evento):

    evento = Evento.query.get_or_404(id_evento)

    db.session.delete(evento)
    db.session.commit()
    return redirect(url_for('evento.lista_evento'))