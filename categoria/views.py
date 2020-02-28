from flask import render_template, url_for, flash, request, redirect, Blueprint
from integradora.categoria.forms import CreateCategoriaForm, UpdateCategoriaForm
from integradora.models import Categoria
from integradora import  db

#from webpersonal.portfolio.image_handler import add_image
#from webpersonal.models import Project
#from webpersonal import db
#from flask_login import login_user, current_user, logout_user, login_required

categoria = Blueprint('categoria', __name__)

#create
@categoria.route('/crear_categoria', methods=['GET','POST']) 
def crear_categoria():
    form = CreateCategoriaForm()

    if form.validate_on_submit():
        categoria = Categoria(nombre=form.nombre.data, icono=form.icono.data)
        db.session.add(categoria)
        db.session.commit()
        return redirect(url_for('categoria.lista_categoria'))

    return render_template('crear-categoria.html', form=form)

@categoria.route('/lista_categoria')
def lista_categoria():
    categorias = Categoria.query.all()
    return render_template('lista-categoria.html', categorias=categorias)#esta parte 

@categoria.route('/<int:id_categoria>/update', methods=['GET', 'POST'])
def update_categoria(id_categoria):
    categoria = Categoria.query.get_or_404(id_categoria)

    form = UpdateCategoriaForm()

    if form.validate_on_submit():
       categoria.nombre = form.nombre.data
       categoria.icono = form.icono.data
       db.session.commit()
       return redirect(url_for('categoria.lista_categoria'))

    elif request.method == 'GET':
        form.nombre.data = categoria.nombre
        form.icono.data = categoria.icono
        

    return render_template('editar-categoria.html', form=form)

@categoria.route('/<int:id_categoria>/delete', methods=['GET','POST'])
def delete_categoria(id_categoria):

    categoria = Categoria.query.get_or_404(id_categoria)

    db.session.delete(categoria)
    db.session.commit()
    return redirect(url_for('categoria.lista_categoria'))

