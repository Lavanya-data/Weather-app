# 🌦️ Weather App — Python Flask + OpenWeatherMap API

A real-time weather application that fetches live weather data using the OpenWeatherMap API.

**Developer:** Setti Lavanya | B.Tech CSDS | QIS College, Ongole  
**Tech Stack:** Python · Flask · HTML · CSS · REST API · JSON

---

## ✨ Features
- 🔍 Search weather for ANY city in the world
- 🌡️ Temperature, Feels Like, Min/Max
- 💧 Humidity, Wind Speed, Pressure, Visibility
- ⚡ Quick search buttons for popular Indian cities
- 🎨 Beautiful dark UI with weather icons
- ⚠️ Proper error handling for wrong city names

## 🛠️ Tech Concepts Used
| Concept | Where Used |
|---|---|
| REST API call | requests.get() to OpenWeatherMap |
| JSON parsing | Extracting data from API response |
| Flask routing | GET and POST methods |
| Jinja2 templating | Displaying data in HTML |
| Error handling | try-except for API errors |

## 🚀 How to Run

### Step 1 — Get FREE API Key
1. Go to https://openweathermap.org/
2. Click Sign Up (free account)
3. Go to API Keys section
4. Copy your API key

### Step 2 — Add your API key
Open `app.py` and replace:
```python
API_KEY = "YOUR_API_KEY_HERE"
```
with your actual key:
```python
API_KEY = "abc123youractualkey"
```

### Step 3 — Install and Run
```bash
pip install flask requests
python app.py
```
Open: **http://127.0.0.1:5000**

---
*Built as Project 3 of 30-day learning challenge · 2026*
