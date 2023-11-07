from flask_app import app
from flask import render_template, request
import requests


@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/weather", mehthods=["POST"])
def weather():
    print(request.form["city"])
    weather_data =requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={request.form['city']}&appid={ff30b97491d94438c36dd6ad2e326993}&units=imperial")
    return weather_data.json()