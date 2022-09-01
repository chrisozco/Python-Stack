from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojo():
    dojo = Dojo.get_all()
    return render_template('dojo_home.html', dojo = dojo)

@app.route('/new_dojo', methods=['POST'])
def new_dojo():
    data = {
        'name' : request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_ninja_info(data)
    return render_template('dojo_info.html', dojo = dojo)

