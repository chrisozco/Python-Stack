from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Recipe:
    db = 'recipes'
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.dateMade = data['dateMade']
        self.under_30 = data['under_30']
        # self.createdAt = data['createdAt']
        # self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM recipe;'
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            recipes.append( cls(row) )
        return recipes

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM recipe WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO recipe (name, description, instruction, dateMade, under_30, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(dateMade)s, %(under_30)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE recipe SET name=%(name)s, description=%(description)s, instruction=%(instruction)s, dateMade=%(dateMade)s, under_30=%(under_30)s WHERE id = %(id)s;'
        print('update', data)
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipe WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def recipeUser(cls, data):
        query = 'SELECT * FROM recipe LEFT JOIN user ON recipe.user_id = user.id WHERE recipe.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        print('recipeuser results', results)
        recipe = []
        for row in results:
            recipe = cls(results[0])
            userData = {
                'id': row['user.id'],
                'firstName': row['firstName'],
                'lastName': row['lastName'],
                'email': row['email'],
                'password': row['password'],
                'createdAt': row['user.createdAt'],
                'updatedAt': row['user.updatedAt']
            }
            print('userdata', userData)
            oneUser = user.User(userData)
            recipe.user = oneUser
            recipe.append(recipe)
            print('allscores', recipe)
        return recipe

    @staticmethod
    def validate(recipe):
        isValid = True
        if len(recipe['name']) < 3:
            isValid = False
            flash('Please enter a Name with at least 3 characters')
        if len(recipe['description']) < 3:
            isValid = False
            flash('Please enter a description with at least 3 characters')
        if len (recipe['instruction']) < 3:
            isValid = False
            flash('Please enter a Instruction with at least 3 characters')
        if len(recipe["dateMade"]) <= 0:
            isValid = False
            flash('Date is required')
        if 'under_30' not in recipe:
            isValid = False
            flash('Does your recipe take less than 30 min?')
        return isValid