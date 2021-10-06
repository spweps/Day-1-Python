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
    



if __name__ == "__main__"
    app.run(debug=True)