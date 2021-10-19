from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Car:
    def __init__(self,data):
        self.id = data["id"]
        self.model = data["model"]
        self.year = data["year"]
        self.description = data["description"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.price = data["price"]
        self.make = data["make"]
        self.cars = []

    @classmethod
    def add_car(cls,data):
        query = "INSERT INTO cars (model, year, description,price,make,user_id) VALUES (%(model)s,%(year)s,%(description)s,%(price)s,%(make)s,%(id)s)"    
        return connectToMySQL("mydb").query_db(query,data)

    @classmethod
    def delete_car(cls,data):
        query = "DELETE FROM cars WHERE id=%(id)s"    
        return connectToMySQL("mydb").query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM cars WHERE id = %(id)s"
        results = connectToMySQL("mydb").query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_user_cars(cls,data):
        query = "SELECT * FROM users JOIN cars ON users.id = cars.user_id WHERE users.id = %(id)s"
        user_cars_db = connectToMySQL("mydb").query_db(query,data)
        
        user = User(user_cars_db[0])

        for uj in user_cars_db:
            car_data = {
                "id":uj["cars.id"],
                "model":uj["model"],
                "make":uj["make"],
                "year":uj["year"],
                "user_id":uj["user_id"],
                "created_at":uj["created_at"],
                "updated_at":uj["updated_at"],
                "price":uj["price"],
                "description":uj["description"]
            }
            user.cars.append(Car(car_data))
        return user
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars;"
        results =  connectToMySQL("mydb").query_db(query)
        all_cars = []
        for row in results:
            all_cars.append(cls(row))
        return all_cars
    

    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL("mydb").query_db(query,data)

    @staticmethod
    def update_car(car):
        query = "UPDATE cars SET description = %(description)s,price= %(price)s,make=%(make)s,year=%(year)s,model=%(model)s WHERE id = %(id)s;"
        results = connectToMySQL("mydb").query_db(query, car)
        return results


    @staticmethod
    def validate_car(car):
        is_valid = True
        if len(car["model"]) <= 1:
            flash("Model needs to be present")
            is_valid = False
        if len(car["price"]) < 1:
            flash("Price needs to be present, cars aren't free!")
            is_valid = False
        if len(car["make"]) <1:
            flash("Make needs to be present")
            is_valid = False
        if len(car["description"]) <1:
            flash ("Description required")
            is_valid = False        
        if len(car["year"]) < 1:
            flash ("Year needed and update required")
            is_valid = False
        if car['year'] == "":
            is_valid = False
            flash("Please enter a valid year")
        return connectToMySQL("mydb")

    @classmethod
    def get_cars_and_users(cls):
        query = "SELECT * FROM users JOIN cars ON users.id = cars.user_id;"
        results =  connectToMySQL("mydb").query_db(query)
        print(results)
        return
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
    def get_seller(cls):
        query = "SELECT * FROM users JOIN cars ON users.id = cars.user_id"
        user_cars_db = connectToMySQL("mydb").query_db(query)
        
        users_and_cars = []

        for uj in user_cars_db:
            user_instance = User(uj)
            car_data = {
                "id":uj["cars.id"],
                "model":uj["model"],
                "make":uj["make"],
                "year":uj["year"],
                "user_id":uj["user_id"],
                "created_at":uj["created_at"],
                "updated_at":uj["updated_at"],
                "price":uj["price"],
                "description":uj["description"]
            }

            user_instance.car = Car(car_data)
            users_and_cars.append(user_instance)

        return users_and_cars
