from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World!."

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/flask")
def flask():
    return "Hi Flask!"

@app.route("/say/michael")
def michael():
    return "Hi Michael"

@app.route("/say/john")
def john():
    return "Hi John!"

if __name__ == "__main__":
    app.run(debug=True)