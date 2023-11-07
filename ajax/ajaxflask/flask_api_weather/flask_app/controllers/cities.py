from flask_app import app
from flask import render_template,request
import requests

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather",methods=["POST"])
def weather():
    weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={request.form['city']}&appid=b01c5ea11547607e9bee74dc4999efea&units=imperial")
    return weather_data.json()