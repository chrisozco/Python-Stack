from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import recipe
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = 'recipes'
    def __init__( self , data ):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.recipes = []

    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM user;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append( cls(row) )
        return users

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM user WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

# This class method will be used for login
# and to verify the user is already in the db
    @classmethod
    def get_email(cls,data):
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user (firstName, lastName, email, password) VALUES (%(firstName)s, %(lastName)s, %(email)s, %(password)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE user SET firstName=%(firstName)s, lastName=%(lastName)s, email=%(email)s, password=%(password)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM user WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def userRecipe(cls, data):
        query = 'SELECT * FROM user LEFT JOIN recipe on user.id = recipe.user_id WHERE user.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        user = cls(results[0])
        for row in results:
            recipeData = {
                'id': row['recipe.id'],
                'name': row['name'],
                'description': row['description'],
                'instruction': row['instruction'],
                'dateMade': row['dateMade'],
                'under_30': row['under_30'],
                'createdAt': row['recipe.createdAt'],
                'updatedAt': row['recipe.updatedAt'],
                'user_id': row['user_id']
            }
            user.recipes.append(recipe.Recipe(recipeData))
        return user

    @staticmethod
    def validate(user):
        isValid = True
        # validates that the email is not already in the system
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            isValid = False
            flash('Email is Already Registered')
        if len(user['firstName']) < 2:
            isValid = False
            flash('Please enter a First Name with at least 2 characters')
        if len(user['lastName']) < 2:
            isValid = False
            flash('Please enter a Last Name with at least 2 characters')
        if len (user['password']) < 6:
            isValid = False
            flash('Please enter a Password with at least 6 characters')
        if not EMAIL_REGEX.match(user['email']):
            isValid = False
            flash('Improper Email Format')
        if user['password'] != user['confirm']:
            isValid = False
            flash('Passwords Do Not Match')
        return isValid
