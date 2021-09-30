from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def checkerboard():
    return render_template("checkerboard.html")

@app.route("/<number>")
def forbyeight(number):
    return render_template("forbyate.html", number= int(number))

@app.route("/<x>/<y>")
def exbywhy(x,y):
    return render_template("xyrando.html", x = int(x), y = int(y))





if __name__ == "__main__":
    app.run(debug=True)