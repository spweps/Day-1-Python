from flask_app import app
from flask import render_template,request,flash,redirect,session
from flask_app.models.painting import Painting
from flask_app.models.user import User


@app.route("/add/painting")
def add_painting():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("painting_add.html",user=User.get_by_id(data))


@app.route("/create/painting", methods=["POST"])
def create_painting():
    if Painting.validate_painting(request.form):
        data = {

        "id":session["user_id"],
        "artist":request.form["artist"],
        "title":request.form["title"],
        "price":request.form["price"],
        "description":request.form["description"]
        }
        Painting.add_painting(data)
    return redirect("/dashboard")



@app.route('/edit/painting/<int:id>')
def edit_painting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("painting_edit.html",painting=Painting.get_one(data),user=User.get_by_id(user_data))

@app.route('/edit/painting/<int:id>', methods=["POST"])
def update_painting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id,
        "description":request.form["description"],
        "price":request.form["price"]
    }
    print(data)
    user_data = {
        "id":session['user_id']
    }
    Painting.update_painting(data)
    return redirect("/dashboard")


@app.route("/delete/<int:id>")
def delete(id):
    if "user_id" not in session:
        flash("Must be logged in to view page")
        return redirect("/")
        
    data = {            
        "id":id
    }
    Painting.delete_painting(data)
    return redirect("/dashboard")

@app.route("/painting/show/<int:id>")
def show_painting(id):
    data={
        "id":id
    }
    painting = Painting.get_one(id)
    return render_template("painting_show.html", painting=painting)
        