from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.sasquatch import Sasquatch

@app.route('/new/sasquatch')
def newSasquatch():
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.get_one(data)
        return render_template('create.html', user=user)

@app.route('/create/sasquatch', methods=['POST'])
def createSasquatch():
    isValid = Sasquatch.validate(request.form)
    if not isValid:
        return redirect('/new/sasquatch')
    else:
        data = {
            'location': request.form['location'],
            'whatHappened': request.form['whatHappened'],
            'date': request.form['date'],
            'numSasquatch': request.form['numSasquatch'],
            'user_id': request.form['user_id']
        }
        Sasquatch.save(data)
        return redirect('/dashboard')

@app.route('/edit/<int:sasquatch_id>')
def editSasquatch(sasquatch_id):
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        dataUser = {
            'id': session['user_id']
        }
        user = User.get_one(dataUser)
        dataSasquatch = {
            'id': sasquatch_id
        }
        sasquatch = Sasquatch.get_one(dataSasquatch)
        return render_template('edit.html', user=user, sasquatch=sasquatch)

@app.route('/sasquatch/update/<int:sasquatch_id>', methods=['POST'])
def updateSasquatch(sasquatch_id):
    isValid = Sasquatch.validate(request.form)
    if not isValid:
        return redirect(f"/edit/{sasquatch_id}")
    else:
        data = {
            'id': sasquatch_id,
            'location': request.form['location'],
            'whatHappened': request.form['whatHappened'],
            'date': request.form['date'],
            'numSasquatch': request.form['numSasquatch'],
        }
        Sasquatch.update(data)
        return redirect('/dashboard')

@app.route('/sasquatch/view/<int:sasquatch_id>')
def viewSasquatch(sasquatch_id):
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        dataUser = {
            'id': session['user_id']
        }
        dataSasquatch = {
            'id': sasquatch_id
        }
        users = User.get_all()
        user = User.get_one(dataUser)
        sasquatch = Sasquatch.get_one(dataSasquatch)
        return render_template('view.html', users=users, user=user, sasquatch=sasquatch)

@app.route('/sasquatch/delete/<int:sasquatch_id>')
def deleteSasquatch(sasquatch_id):
    dataSasquatch = {
        'id': sasquatch_id
    }
    Sasquatch.delete(dataSasquatch)
    return redirect('/dashboard')
