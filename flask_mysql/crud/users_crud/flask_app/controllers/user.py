from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template('users.html', users = User.get_all())

@app.route('/users_add', methods=['POST'])
def new_user():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/users/new')
def result():
    return render_template('create.html')

@app.route('/users/<int:users_id>/view')
def viewUser(users_id):
    data = {
        'id': users_id
    }
    the_user = User.get_one(data)
    return render_template('singleuser.html', users = the_user)

@app.route('/users/<int:users_id>/edit')
def editUser(users_id):
    data = {
        'id': users_id
    }
    return render_template('edituser.html', users = User.get_one(data))

@app.route('/users/<int:users_id>/update', methods=['post'])
def updateTrainer(users_id):
    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update(data)
    return redirect(f'/users/{users_id}/view')

@app.route('/users/<int:users_id>/delete')
def deleteUser(users_id):
    data = {
        'id': users_id
    }
    User.delete(data)
    return redirect('/')