from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import ToDo


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form.get('task'):
        todo = ToDo()
        todo.task = request.form.get('task')
        db.session.add(todo)
        db.session.commit()
    todos = ToDo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/complete/<id>')
def complete(id):
    if ToDo.query.get(id):
        todo = ToDo.query.get(id)
        todo.is_active = not(todo.is_active)
        db.session.add(todo)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<id>')
def delete(id):
    if ToDo.query.get(id):
        db.session.delete(ToDo.query.get(id))
        db.session.commit()
    return redirect(url_for('index'))