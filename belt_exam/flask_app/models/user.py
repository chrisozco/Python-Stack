from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import sasquatch
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = 'belt_exam'
    def __init__( self , data ):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.sasquatch = []

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
    def userSasquatch(cls, data):
        query = 'SELECT * FROM user LEFT JOIN sasquatch on user.id = sasquatch.user_id WHERE user.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        user = cls(results[0])
        for row in results:
            sasquatchData = {
                'id': row['sasquatch.id'],
                'location': row['location'],
                'whatHappened': row['whatHappened'],
                'date': row['date'],
                'numSasquatch': row['numSasquatch'],
                'createdAt': row['sasquatch.createdAt'],
                'updatedAt': row['sasquatch.updatedAt'],
                'user_id': row['user_id']
            }
            user.sasquatch.append(sasquatch.Sasquatch(sasquatchData))
        return user

    @staticmethod
    def validate(user):
        isValid = True
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
        if len (user['password']) < 8:
            isValid = False
            flash('Please enter a Password with at least 8 characters')
        if not EMAIL_REGEX.match(user['email']):
            isValid = False
            flash('Improper Email Format')
        if user['password'] != user['confirm']:
            isValid = False
            flash('Passwords Do Not Match')
        return isValid
