from flask import Flask, render_template, request, redirect,
from meme import Meme

app = Flask(__name__)

@app.route("/")
def index():
    memes = Meme.get_all_memes()
    return render_template("serversqlconnection.html", memes=memes)


@app.route("/insertmeme", methods = ["POST"])
def insert_meme():
    data = {
        "name":  request.form["name"],
        "meme_url": request.form["meme_url"]
    }
    Meme.insert_meme(data)
    return redirect("/")
    
@app.route("/delte/<int:id>")
def delete(id):
    data = {
        "id": id
    }
    Meme.delete_meme(data)
    return redirect("/")

@app.route("/edit/<int:id>")
def edit_meme(id):
    data = {
        "id": id
    }
    meme = Meme.get_meme(data)
    return render_template("editmeme.html", meme=meme)

@app.route("/editmeme/<int:id>", methods = ["POST"])
def update_meme_db(id):
    data = {
        "name":  request.form["name"],
        "meme_url": request.form["meme_url"],
        "id": id
    }
    Meme.update_meme(data)
    return redirect("/")


if __name__ == "__main__"
    app.run(debug=True)