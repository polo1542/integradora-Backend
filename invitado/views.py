from flask import render_template, url_for, flash, request, redirect, Blueprint, current_app
from integradora.invitado.forms import CreateInvitadoForm, UpdateInvitadoForm
from integradora.models import Invitado
from integradora import  db
import os 
from PIL import Image


invitado = Blueprint('invitado', __name__)

@invitado.route('/crear_invitado', methods=['GET', 'POST'])
def crear_invitado():
    form = CreateInvitadoForm()

    if form.validate_on_submit():
        imagen_file = form.imagen.data
        imagen_nombre = imagen_file.filename
        imagen_nombre = imagen_nombre.replace(" ", "-")
        imagen_ruta = os.path.join(current_app.root_path, 'static/Imagen', imagen_nombre)
        pic = Image.open(imagen_file)
        pic.save(imagen_ruta)
        invitado = Invitado(nombre=form.nombre.data, apellido=form.apellido.data, descripcion=form.descripcion.data, evento_id=form.evento_id.data)
        invitado.imagen = imagen_nombre
        db.session.add(invitado)
        db.session.commit()
        return redirect(url_for('invitado.lista_invitado'))

    return render_template('crear-invitado.html', form=form)

@invitado.route('/lista_invitados')############
def lista_invitado():
    invitados = Invitado.query.all()
    return render_template('lista-invitado.html', invitados=invitados)

@invitado.route('/<int:id_invitado>/update', methods=['GET', 'POST'])
def update_invitado(id_invitado):
    invitado = Invitado.query.get_or_404(id_invitado)

    form = UpdateInvitadoForm()
    imagen_actual = invitado.imagen

    if form.validate_on_submit():
        invitado.nombre = form.nombre.data
        invitado.apellido = form.apellido.data
        invitado.descripcion = form.descripcion.data
        if form.imagen.data is not None:
            imagen_file = form.imagen.data
            imagen_nombre = imagen_file.filename
            imagen_nombre = imagen_nombre.replace(" ", "-")
            imagen_ruta = os.path.join(current_app.root_path, 'static\Imagen', imagen_nombre)
            pic = Image.open(imagen_file)
            pic.save(imagen_ruta)
            invitado.imagen = imagen_nombre 
        db.session.commit()
        return redirect(url_for('invitado.lista_invitado'))

    elif request.method == 'GET':
        form.nombre.data = invitado.nombre
        form.apellido.data = invitado.apellido
        form.descripcion.data = invitado.descripcion
        form.imagen.data = invitado.imagen


    return render_template('editar-invitado.html', form=form)

@invitado.route('/<int:id_invitado>/delete', methods=['GET','POST'])
def delete_invitado(id_invitado):

    invitado = Invitado.query.get_or_404(id_invitado)

    db.session.delete(invitado)
    db.session.commit()
    return redirect(url_for('invitado.lista_invitado'))