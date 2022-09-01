from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/recipes/new')
def newRecipe():
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.get_one(data)
        return render_template('recipe_create.html', user=user)

@app.route('/create/recipe', methods=['POST'])
def createRecipe():
    isValid = Recipe.validate(request.form)
    if not isValid:
        return redirect('/recipes/new')
    else:
        data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'instruction': request.form['instruction'],
            'dateMade': request.form['dateMade'],
            'under_30': request.form['under_30'],
            'user_id': request.form['user_id']
        }
        Recipe.save(data)
        return redirect('/recipes')

@app.route('/recipe/edit/<int:recipe_id>')
def editRecipe(recipe_id):
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        dataUser = {
            'id': session['user_id']
        }
        user = User.get_one(dataUser)
        dataRecipe = {
            'id': recipe_id
        }
        recipe = Recipe.get_one(dataRecipe)
        return render_template('recipe_edit.html', user=user, recipe=recipe)

@app.route('/recipes/update/<int:recipe_id>', methods=['POST'])
def updateRecipe(recipe_id):
    isValid = Recipe.validate(request.form)
    if not isValid:
        return redirect('/recipes/new')
    else:
        data = {
            'id': recipe_id,
            'name': request.form['name'],
            'description': request.form['description'],
            'instruction': request.form['instruction'],
            'dateMade': request.form['dateMade'],
            'under_30': request.form['under_30'],
        }
        Recipe.update(data)
        return redirect('/recipes')

@app.route('/recipe/view/<int:recipe_id>')
def viewRecipe(recipe_id):
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        dataUser = {
            'id': session['user_id']
        }
        dataRecipe = {
            'id': recipe_id
        }
        users = User.get_all()
        user = User.get_one(dataUser)
        recipe = Recipe.get_one(dataRecipe)
        return render_template('recipe_view.html', users=users, user=user, recipe=recipe)

@app.route('/recipe/delete/<int:recipe_id>')
def deleteRecipe(recipe_id):
    dataRecipe = {
        'id': recipe_id
    }
    Recipe.delete(dataRecipe)
    return redirect('/recipes')
