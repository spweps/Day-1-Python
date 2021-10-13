from flask_app import app
from flask import render_template,request,flash,redirect,session
from flask_app.models.painting import Painting


@app.route("/add/painting",methods=["POST"])
def add_painting():
    if Painting.validate_painting(request.form):
        data = {
            "artist":request.form["artist"],
            "title":request.form["title"],
            "price":request.form["price"]
        }
        Painting.add_painting(data)
        return redirect("/add/painting")
    else:
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