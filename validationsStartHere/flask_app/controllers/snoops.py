from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.snoop import Snoop

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validatevictim", methods=["POST"])
def validate_victim():
    if Snoop.validate_victim(request.form):
        return redirect("/success")
    else:
        return redirect("/")

@app.route("/sucess")
def success():
    return render_template("success.html")