from flask_app import app
from flask import render_template,flash,redirect,request, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=["POST"])
def register():
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "email":request.form["email"],
        "password":pw_hash
    }
    user_id = User.insert_user(data)
    session["user_id"] = user_id
    flash("User created!")
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    data = {"email":request.form["email"]}
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password,request.form["password"]):
        flash("Invalid Email/Password")
        return redirect("/")
    session["user_id"] = user_in_db.id
    return redirect("/secretpage")

@app.route("/secretpage")
def secret_page():
    if "user_id" not in session:
        flash("Must be logged in.")
        return redirect("/")
    else:
        return render_template("secretpage.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out")
    return redirect("/")
