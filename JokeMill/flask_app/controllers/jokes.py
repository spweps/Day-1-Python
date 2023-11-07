from flask_app import app
from flask import render_template,request,flash,redirect,session
from flask_app.models.joke import Joke

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Must be logged in to view page")
        return redirect("/")

    users_jokes = Joke.get_users_jokes()
    return render_template("dashboard.html",users_jokes=users_jokes)

@app.route("/insertjoke",methods=["POST"])
def insert_joke():
    if Joke.validate_joke(request.form):
        data = {
            "comedian":request.form["comedian"],
            "joke":request.form["joke"],
            "id":session["user_id"]
        }
        Joke.insert_joke(data)
        return redirect("/dashboard")
    else:
        return redirect("/dashboard")

@app.route("/user/<int:id>")
def user(id):
    if "user_id" not in session:
        flash("Must be logged in to view page")
        return redirect("/")

    data = {            
        "id":id
    }
    one_user_jokes = Joke.get_user_jokes(data)
    return render_template("userpage.html", one_user_jokes=one_user_jokes)

@app.route("/delete/<int:id>")
def delete(id):
    if "user_id" not in session:
        flash("Must be logged in to view page")
        return redirect("/")
        
    data = {            
        "id":id
    }
    Joke.delete_joke(data)
    return redirect("/dashboard")