from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html") #from template folder--index is referenced as a route

@app.route("/monsters/<monster>")  #<monster> is indicated in the URL where you choose the monster--bootstrapping
def monster_page(monster):
    print(monster)
    return render_template("monster.html")

if __name__ == "__main__":
    app.run(debug=True)