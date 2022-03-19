from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash 

class Recipe: 
    db = 'recipe_schema'
    def __init__(self,data): 
        self.id = data['id']
        self.name = data['name'] 
        self.description = data['description']
        self.instruction = data['instruction']
        self.time = data['time']
        self.dateMade = data['dateMade']
        self.user_id = data['user_id']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        

    @staticmethod
    def validateRecipe(recipe):
        is_valid = True 
        if len(recipe['name']) < 3:
            flash("Name must be at least 3 characters.", "recipe")
            is_valid = False
        if len(recipe['description']) < 1:
            flash("Description must be at least 3 characters.", "recipe")
            is_valid = False
        if len(recipe['instruction']) < 1:
            flash("Instructions must be at least 3 characters.", "recipe")
            is_valid = False
        return is_valid

    @classmethod
    def getAll(cls):
            query ="SELECT * FROM recipe;"
            results = connectToMySQL(cls.db).query_db(query)
            recipes = []

            for r in results:
                recipes.append(cls(r))
            return recipes 
    
    @classmethod 
    def getOne(cls, data):
        query = 'SELECT * FROM recipe WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False 
        return cls(results[0]) 


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipe ( name , description , instruction , time, dateMade, user_id ) VALUES ( %(name)s , %(description)s , %(instruction)s , %(time)s, %(dateMade)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db( query, data )
    

    @classmethod
    def update(cls, data):
        query = "UPDATE recipe SET name=%(name)s, description=%(description)s, instruction=%(instruction)s, time=%(time)s, dateMade=%(dateMade)s, updatedAt=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)


    @classmethod 
    def delete (cls, data): 
        query = "DELETE FROM recipe WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)