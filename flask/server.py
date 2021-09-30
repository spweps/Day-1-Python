from flask import Flask, render_template
import facts

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html") #from template folder--index is referenced as a route

@app.route("/monsters/<monster>")  #<monster> is indicated in the URL where you choose the monster--bootstrapping
def monster_page(monster):
    if monster = "dracula":
        return render_template("monster.html", monster_name=monster.capitalize(), facts = facts.dracula_facts) #facts = f"{facts.monster}_facts"

if __name__ == "__main__":
    app.run(debug=True)