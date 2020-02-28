from flask import render_template, url_for, flash, request, redirect, Blueprint
from integradora.regalo.forms import CreateRegaloForm, UpdateRegaloForm
from integradora.models import Regalo
from integradora import  db

regalo = Blueprint('regalo', __name__)

@regalo.route('/crear_regalo', methods=['GET', 'POST'])
def crear_regalo():
    form = CreateRegaloForm()

    if form.validate_on_submit():
        regalo = Regalo(nombre=form.nombre.data)
        db.session.add(regalo)
        db.session.commit()
        return redirect(url_for('regalo.lista_regalo'))

    return render_template('crear-regalo.html', form=form)

@regalo.route('/lista_regalos')##############
def lista_regalo():
    regalos = Regalo.query.all()
    return render_template('lista-regalo.html', regalos=regalos)

@regalo.route('/<int:id_regalo>/update', methods=['GET', 'POST'])
def update_regalo(id_regalo):
    regalo = Regalo.query.get_or_404(id_regalo)

    form = UpdateRegaloForm()

    if form.validate_on_submit():
        regalo.nombre = form.nombre.data
        db.session.commit()
        return redirect(url_for('regalo.lista_regalo'))

    elif request.method == 'GET':
        form.nombre.data = regalo.nombre
        

    return render_template('editar-regalo.html', form=form)

@regalo.route('/<int:id_regalo>/delete', methods=['GET','POST'])
def delete_regalo(id_regalo):

    regalo = Regalo.query.get_or_404(id_regalo)

    db.session.delete(regalo)
    db.session.commit()
    return redirect(url_for('regalo.lista_regalo'))