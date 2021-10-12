from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.jokes = []

    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id=%(id)s"
        return connectToMySQL("joke_mill").query_db(query,data)    
    

    @staticmethod
    def validate_update(user):
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True
        if len(user["first_name"]) < 1:
            flash("First Name is required")
            is_valid = False
        if len(user["last_name"]) < 1:
            flash("Last Name is required")
            is_valid = False
        if not email_regex.match(user['email']): 
            flash("Invalid email address")
            is_valid = False
        
        
        return is_valid
        
