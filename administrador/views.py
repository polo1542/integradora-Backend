from flask import render_template, url_for, flash, request, redirect, Blueprint, current_app
from integradora.administrador.forms import CreateAdministradorForm, UpdateAdministradorForm
from integradora.models import User
from integradora import  db
import os 
from PIL import Image


administrador = Blueprint('administrador', __name__)

@administrador.route('/crear_administrador', methods=['GET', 'POST'])
def crear_administrador():
    form = CreateAdministradorForm()

    if form.validate_on_submit():
        imagen_file = form.imagen.data
        imagen_nombre = imagen_file.filename
        imagen_nombre = imagen_nombre.replace(" ", "-")
        imagen_ruta = os.path.join(current_app.root_path, 'static/Imagen', imagen_nombre)
        pic = Image.open(imagen_file)
        pic.save(imagen_ruta)
        administrador = User(profile_image=form.profile_image.data, email=form.email.data, username=form.username.data, password_hash=form.password_hash.data)
        administrador.imagen = imagen_nombre
        db.session.add(administrador)
        db.session.commit()
        return redirect(url_for('administrador.lista_admin'))

    return render_template('crear-admin.html', form=form)

@administrador.route('/lista_administrados')############
def lista_administradores():
    administrados = User.query.all()
    return render_template('administrador-admin.html', administrados=administrados)

@administrador.route('/<int:id_administrador>/update', methods=['GET', 'POST'])
def update_administrador(id_administrador):
    administrador = User.query.get_or_404(id_administrador)

    form = UpdateAdministradorForm()
    imagen_actual = administrador.imagen

    if form.validate_on_submit():
        administrador.email = form.email.data
        administrador.username = form.username.data
        administrador.password_hash = form.password_hash.data
        if form.imagen.data is not None:
            imagen_file = form.imagen.data
            imagen_nombre = imagen_file.filename
            imagen_nombre = imagen_nombre.replace(" ", "-")
            imagen_ruta = os.path.join(current_app.root_path, 'static\Imagen', imagen_nombre)
            pic = Image.open(imagen_file)
            pic.save(imagen_ruta)
            administrador.imagen = imagen_nombre 
        db.session.commit()
        return redirect(url_for('administrador.lista_admin'))

    elif request.method == 'GET':
        form.email.data = administrador.email
        form.username.data = administrador.username
        form.password_hash.data = administrador.password_hash
        form.profile_image.data = administrador.profile_image


    return render_template('editar-administrador.html', form=form)

@administrador.route('/<int:id_administrador>/delete', methods=['GET','POST'])
def delete_administrador(id_administrador):

   administrador = User.query.get_or_404(id_administrador)

    db.session.delete(administrador)
    db.session.commit()
    return redirect(url_for('administrador.lista_admin'))