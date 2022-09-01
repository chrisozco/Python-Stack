from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def user():
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        return redirect('/recipes')

@app.route('/register',methods=['POST'])
def register():
    isValid = User.validate(request.form)
    if not isValid:
        return redirect('/')
    else:
        newUser = {
            'firstName' : request.form['firstName'],
            'lastName' : request.form['lastName'],
            'email' : request.form['email'],
            'password' : bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(newUser)
        if not id:
            flash('Oops! Something Went Wrong')
            return redirect('/')
        else:
            session['user_id'] = id
            flash('Welcome!')
            return redirect('/recipes')

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.get_email(data)
    if not user:
        flash('Please register!')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Incorrect Password, Please Try Again!')
        return redirect('/')
    else:
        session['user_id'] = user.id
        flash('Welcome!')
        return redirect('/recipes')

@app.route('/recipes')
def recipesDashboard():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        users = User.get_all()
        user = User.get_one(data)
        recipes = Recipe.get_all()
        return render_template('recipes_page.html', user = user, users=users, recipes=recipes)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')