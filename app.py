# ============================================================
#  WEATHER APP — Built with Python Flask + OpenWeatherMap API
#  Developer : Setti Lavanya
#  Tech Stack: Python, Flask, HTML, CSS, API, JSON
# ============================================================

# ── WHAT IS AN API? ──
# API = Application Programming Interface
# It is like a waiter in a restaurant:
# You (your app) ask the waiter (API) for food (data)
# The kitchen (server) prepares it and waiter brings it back
# Here we ask OpenWeatherMap API for weather data of any city

from flask import Flask, render_template, request
import requests  # This library helps us call external APIs
import os

app = Flask(__name__)

# ── YOUR API KEY ──
# This is like a password to use OpenWeatherMap's service
# We will get this key for FREE in Step 1 of setup
# Replace the string below with your actual key
API_KEY = "f5f78ab811ce925f668e512cd23c5fa1"

# ── BASE URL of OpenWeatherMap API ──
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    This function calls the OpenWeatherMap API
    and returns weather data for the given city.
    
    Parameters: city (string) - name of the city
    Returns: dictionary with weather info, or None if error
    """
    try:
        # Build the request with parameters
        # q = city name
        # appid = our API key
        # units = metric means Celsius (imperial = Fahrenheit)
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"   # Change to "imperial" for Fahrenheit
        }

        # Make the API call — this sends a request to OpenWeatherMap
        response = requests.get(BASE_URL, params=params)

        # Check if request was successful (status code 200 = success)
        if response.status_code == 200:

            # Convert the response to JSON (Python dictionary)
            data = response.json()

            # Extract only the data we need
            weather_info = {
                "city":        data["name"],
                "country":     data["sys"]["country"],
                "temperature": round(data["main"]["temp"]),
                "feels_like":  round(data["main"]["feels_like"]),
                "humidity":    data["main"]["humidity"],
                "description": data["weather"][0]["description"].title(),
                "icon":        data["weather"][0]["icon"],
                "wind_speed":  round(data["wind"]["speed"] * 3.6),  # m/s to km/h
                "pressure":    data["main"]["pressure"],
                "visibility":  round(data.get("visibility", 0) / 1000, 1),  # m to km
                "min_temp":    round(data["main"]["temp_min"]),
                "max_temp":    round(data["main"]["temp_max"]),
            }
            return weather_info, None

        elif response.status_code == 404:
            return None, "City not found! Please check the city name."

        elif response.status_code == 401:
            return None, "Invalid API key! Please check your API key."

        else:
            return None, f"Error {response.status_code}: Could not fetch weather data."

    except requests.exceptions.ConnectionError:
        return None, "No internet connection! Please check your network."

    except Exception as e:
        return None, f"Something went wrong: {str(e)}"


def get_weather_emoji(description):
    """Returns an emoji based on weather description"""
    desc = description.lower()
    if "clear" in desc:       return "☀️"
    elif "cloud" in desc:     return "☁️"
    elif "rain" in desc:      return "🌧️"
    elif "drizzle" in desc:   return "🌦️"
    elif "thunder" in desc:   return "⛈️"
    elif "snow" in desc:      return "❄️"
    elif "mist" in desc or "fog" in desc: return "🌫️"
    elif "haze" in desc:      return "😶‍🌫️"
    else:                     return "🌡️"


# ── HOME PAGE ──
@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    city = ""

    # POST means user submitted the search form
    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if city:
            weather, error = get_weather(city)
            if weather:
                weather["emoji"] = get_weather_emoji(weather["description"])
        else:
            error = "Please enter a city name!"

    # Default city on first load
    if request.method == "GET":
        weather, error = get_weather("Visakhapatnam")
        if weather:
            weather["emoji"] = get_weather_emoji(weather["description"])
            city = "Visakhapatnam"

    return render_template("index.html", weather=weather, error=error, city=city)


# ── Run the app ──
if __name__ == "__main__":
    app.run(debug=True)
