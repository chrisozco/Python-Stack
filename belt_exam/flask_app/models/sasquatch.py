from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Sasquatch:
    db = 'belt_exam'
    def __init__( self , data ):
        self.id = data['id']
        self.location = data['location']
        self.whatHappened = data['whatHappened']
        self.date = data['date']
        self.numSasquatch = data['numSasquatch']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM sasquatch;'
        results = connectToMySQL(cls.db).query_db(query)
        sasquatches = []
        for row in results:
            sasquatches.append( cls(row) )
        return sasquatches

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM sasquatch WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO sasquatch (location, whatHappened, date, numSasquatch, user_id) VALUES (%(location)s, %(whatHappened)s, %(date)s, %(numSasquatch)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE sasquatch SET location = %(location)s, whatHappened = %(whatHappened)s, date = %(date)s, numSasquatch = %(numSasquatch)s WHERE id = %(id)s'
        print('update', data)
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM sasquatch WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def sasquatchUser(cls, data):
        query = 'SELECT * FROM sasquatch LEFT JOIN user ON sasquatch.user_id = user.id WHERE sasquatch.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        print('sasquatchuser results', results)
        sasquatch = []
        for row in results:
            sasquatch = cls(results[0])
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
            sasquatch.user = oneUser
            sasquatch.append(sasquatch)
            print('allsasquatches', sasquatch)
        return sasquatch

    @staticmethod
    def validate(sasquatch):
        isValid = True
        if len(sasquatch['location']) < 2:
            isValid = False
            flash('Please enter a Location with at least 2 characters!')
        if len(sasquatch['whatHappened']) < 3:
            isValid = False
            flash('You cant tell an awsome story with only 3 letters!!')
        if len(sasquatch["date"]) <= 0:
            isValid = False
            flash('Date is required')
        if len(sasquatch["numSasquatch"]) < 1:
            isValid = False
            flash('How many did you see?')
        return isValid