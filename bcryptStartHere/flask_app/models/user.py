from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def insert_user(cls,data):
        query = "INSERT INTO users (email,password) VALUES (%(email)s,%(password)s)"
        return connectToMySQL("users_db").query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "Select * from users  where email = %(email)s"
        user_db =  connectToMySQL("users_db").query_db(query,data)

        if len(user_db) < 1:
            return False
        return User(user_db[0])