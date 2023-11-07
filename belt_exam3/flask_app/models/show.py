from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Show:
    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.release_date = data["release_date"]
        self.description = data["description"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.network = data["network"]
        self.shows = []

    @classmethod
    def add_show(cls,data):
        query = "INSERT INTO shows (title, release_date, description,network,user_id) VALUES (%(title)s,%(release_date)s,%(description)s,%(network)s,%(id)s)"    
        return connectToMySQL("mydb").query_db(query,data)

    @classmethod
    def delete_show(cls,data):
        query = "DELETE FROM shows WHERE id=%(id)s"    
        return connectToMySQL("mydb").query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM shows WHERE id = %(id)s"
        results = connectToMySQL("mydb").query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_user_shows(cls,data):
        query = "SELECT * FROM users JOIN shows ON users.id = shows.user_id WHERE users.id = %(id)s"
        user_shows_db = connectToMySQL("mydb").query_db(query,data)
        
        user = User(user_shows_db[0])

        for uj in user_shows_db:
            show_data = {
                "id":uj["shows.id"],
                "title":uj["title"],
                "network":uj["network"],
                "release_date":uj["release_date"],
                "user_id":uj["user_id"],
                "created_at":uj["created_at"],
                "updated_at":uj["updated_at"],
                "description":uj["description"]
            }
            user.shows.append(Show(show_data))
        return user
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows;"
        results =  connectToMySQL("mydb").query_db(query)
        all_shows = []
        for row in results:
            all_shows.append(cls(row))
        return all_shows
    

    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL("mydb").query_db(query,data)

    @staticmethod
    def update_show(show):
        query = "UPDATE shows SET description = %(description)s,network= %(network)s,title=%(title)s,release_date=%(release_date)s WHERE id = %(id)s;"
        results = connectToMySQL("mydb").query_db(query, show)
        return results


    @staticmethod
    def validate_show(show):
        is_valid = True
        if len(show["title"]) <= 3:
            flash("Title needs to be present")
            is_valid = False
        if len(show["network"]) < 3:
            flash("Network needs to be present")
            is_valid = False
        if len(show["description"]) <3:
            flash ("Description required")
            is_valid = False        
        if len(show["release_date"]) < 1:
            flash ("Release date required")
            is_valid = False
        return connectToMySQL("mydb")

    # @classmethod
    # def get_cars_and_users(cls):
    #     query = "SELECT * FROM users JOIN cars ON users.id = cars.user_id;"
    #     results =  connectToMySQL("mydb").query_db(query)
    #     print(results)
    #     return
        # all_users_cars = []
    #     for row in results:
    #         all_users_cars.append(cls(row))
        # return cars_and_users
    
    # @classmethod
    # def get_seller(cls):
    #     query = "SELECT * FROM users JOIN cars ON users.id = cars.user_id;"
    #     results =  connectToMySQL("mydb").query_db(query)
    #     all_users_cars = []
    #     for row in results:
    #         all_users_cars.append(cls(row))
        # return all_users_cars

    @classmethod
    def get_poster(cls):
        query = "SELECT * FROM users JOIN shows ON users.id = shows.user_id"
        user_shows_db = connectToMySQL("mydb").query_db(query)
        
        users_and_shows = []

        for uj in user_shows_db:
            user_instance = User(uj)
            show_data = {
                "id":uj["show.id"],
                "title":uj["title"],
                "network":uj["network"],
                "release_date":uj["release_date"],
                "user_id":uj["user_id"],
                "created_at":uj["created_at"],
                "updated_at":uj["updated_at"],
                "description":uj["description"]
            }

            user_instance.show = Show(show_data)
            users_and_shows.append(user_instance)

        return users_and_shows