from flask_app import app
from flask import render_template,request,flash,redirect,session
from flask_app.models.car import Car
from flask_app.models.user import User


@app.route("/add/car")
def add_car():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("sell_car.html",user=User.get_by_id(data))


@app.route("/create/car", methods=["POST"])
def create_car():
    if Car.validate_car(request.form):
        data = {

        "id":session["user_id"],
        "model":request.form["model"],
        "year":request.form["year"],
        "description":request.form["description"],
        "price":request.form["price"],
        "make":request.form["make"]
        }
        Car.add_car(data)
    return redirect("/dashboard")


@app.route('/edit/car/<int:id>')
def edit_car(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_car.html",car=Car.get_one(data),user=User.get_by_id(user_data))

@app.route('/edit/car/<int:id>', methods=["POST"])
def update_car(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id,
        "model":request.form["model"],
        "year":request.form["year"],
        "description":request.form["description"],
        #"seller":request.form["user_id"],
        "price":request.form["price"],
        "make":request.form["make"]
    }
    print(data)
    user_data = {
        "id":session['user_id']
    }
    Car.update_car(data)
    return redirect("/dashboard")


@app.route("/delete/<int:id>")
def delete(id):
    if "user_id" not in session:
        flash("Must be logged in to view page")
        return redirect("/")
        
    data = {            
        "id":id
    }
    Car.delete_car(data)
    return redirect("/dashboard")

@app.route("/show/<int:id>")
def show_car(id):
    data={
        "id":id
    }
    car = Car.get_one(data)
    return render_template("show_car.html", car=car)

@app.route('/destroy/car/<int:id>')
def destroy_car(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Car.destroy(data)
    return redirect('/dashboard')
