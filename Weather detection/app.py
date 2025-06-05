from flask import Flask,render_template,request
import requests

app=Flask(__name__)

API_KEY="60c7ebdb108a4fe1d997c2b88be97c47"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_weather", methods=["POST"])
def get_weather():
    city = request.form.get("city")

    if not city or not validate_city_name(city):
        return render_template("index.html",error="Please enter a valid city name")

    base_url = ""
    params = {
        "q":city,
        "appid": API_KEY,
        "units": "metric"
    }
response = requests.get(base_url, params=params)

if response.status_code ==200:
    data = response.json()
    wether = {
        "city" : data["name"],
        "description": data["main"]["temp"],
        "temperature": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "icon":
    }