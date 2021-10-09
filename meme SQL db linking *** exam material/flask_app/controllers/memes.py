from flask_app import app
from flask import render_template, request, redirect
from meme import Meme
from flask_app.models.meme import Meme

@app.route("/")
def indes():
    memes = Meme.get_all_memes()
    return render_template("serversqlconnection.html")

@app.route("/insertmeme", methods = ["POST"])
def insert_meme():
    data = {
        "name": request.form["name"]
        "meme_url": request.form["meme_url"]
    }
    Meme.insert_meme(data)
    return redirect("/")