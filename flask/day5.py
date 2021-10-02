from flask import Flask, render_template, request, redirect, session #sets cookies--must set up secret key
app = Flask(__name__)
app.secret_key = "shh" #create a random set of letters and numbers


@app.route("/")
def index():
    if "voters" not in session: #checks to see if the user has been here before
        session["voters"] = [] #creates empty list and adds voters

    if "votes" not in session:
        session["votes"] = {"total":0, "Toy Story":0, "Monsters Inc":0, "The Incredibles":0}


    return render_template("day5.html")

@app.route("/vote", methods=["POST"])
def vote():
    #temp_user = {
    #   "name": request.form["name"]
    #   "age": request.form["age"]
    #   "movie": request.form["movie"]
    # }
    temp_user = {} #creates a dictionary and inserts data
    temp_user["name"] = request.form["name"]
    temp_user["age"] = request.form["age"]
    temp_user["movie"] = request.form["movie"]
    #session["voters"].append(temp_user) #appending to session does no tstick
    #session.modified = True --only if you have append a temp various
    voters = session["voters"]
    voters.append(temp_user)
    session["voters"] = voters
    session["votes"]["total"] += 1 #static count for all counts
    session["votes"]
    return redirect("/results")
    #DO NOT RUN render_template with "forms"--reprocesses data

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

@app.route("/results")
def results():
    return render_template("results.html", voters=session["voters"])

if __name__=="__main__":
    app.run(debug=True)