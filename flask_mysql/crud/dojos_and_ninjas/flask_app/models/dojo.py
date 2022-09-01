from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    db = 'dojos_and_ninjas'
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninja = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojo;'
        results = connectToMySQL(cls.db).query_db(query)
        dojo = []
        for row in results:
            dojo.append( cls(row) )
        return dojo

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM dojo WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])


    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojo (name) VALUES (%(name)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE dojo SET name=%(name)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojo WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_ninja_info(cls, data ):
        query = "SELECT * FROM dojo LEFT JOIN ninjas on dojo.id = ninjas.dojo_id WHERE dojo.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            student = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            print("Results", results)
            print("Dojo", dojo)
            dojo.ninja.append( Ninja(student) )
        return dojo
