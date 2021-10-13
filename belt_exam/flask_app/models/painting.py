from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Painting:
    def __init__(self,data):
        self.id = data["id"]
        self.artist = data["artist"]
        self.painting = data["painting"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.price = data["price"]

    @classmethod
    def add_painting(cls,data):
        query = "INSERT INTO paintings (artist,title,price,user_id) VALUES (%(artist)s,%(title)s,%(price)s,%(id)s)"    
        return connectToMySQL("belt_exam").query_db(query,data)

    @classmethod
    def delete_painting(cls,data):
        query = "DELETE FROM paintings WHERE id=%(id)s"    
        return connectToMySQL("belt_exam").query_db(query,data)

    @staticmethod
    def validate_painting(painting):
        is_valid = True
        if len(painting["artist"]) <= 3:
            flash("Artist needs to be 3 or more characters")
            is_valid = False
        if len(painting["description"]) <= 10:
            flash("Description needs to be 10 or more characters")
            is_valid = False
        if len(painting["price"]) <1:
            flash("Price needs to be more than zero")
            is_valid = False        
        return connectToMySQL("belt_exam")
    
