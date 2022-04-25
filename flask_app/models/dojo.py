from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, dojo_data):
        self.id = dojo_data['id']
        self.name = dojo_data['name']
        self.dojo_location = dojo_data['dojo_location']
        self.favorite_language = dojo_data['favorite_language']
        self.comment = dojo_data['comment']
        self.created_at = dojo_data['created_at']
        self.updated_at = dojo_data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        dojo_results = connectToMySQL("dojo_survey").query_db(
            query
        )  
        dojos = []
        for dojo in dojo_results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, dojo_location, favorite_language, comment) VALUES (%(name)s,%(dojo_location)s,%(favorite_language)s, %(comment)s);"
        return connectToMySQL("dojo_survey").query_db(query, data)

    @classmethod
    def get_one(cls, data):
        print('data - ', data)
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        result_from_db = connectToMySQL("dojo_survey").query_db(query, data)
        print('result_from_db - ', result_from_db)
        return cls(result_from_db[0])
    
    @staticmethod
    def validate_dojo(dojo):
        print('dojo -', dojo)
        is_valid = True 
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if (dojo['dojo_location']) == 'select':
            flash("Please select a location.")
            is_valid = False
        if (dojo['favorite_language']) == 'select':
            flash("Please select a language.")
            is_valid = False
        if len(dojo['comment']) < 10:
            flash("Comment must be at least 10 characters.")
            is_valid = False
        return is_valid