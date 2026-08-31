# ==========================================
# Day 23 - Weather API App
# 30 Days Python GitHub Project Challenge
# ==========================================

import requests


print("======================================")
print("          WEATHER API APP")
print("======================================")


# ==========================================
# API SETTINGS
# ==========================================

API_KEY = "YOUR_API_KEY"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ==========================================
# Get City
# ==========================================

city = input("\nEnter city name: ").strip()


# ==========================================
# API Request
# ==========================================

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}


try:

    response = requests.get(
        BASE_URL,
        params=params
    )

    data = response.json()


except requests.exceptions.RequestException:

    print("\n❌ Internet connection error.")
    exit()


# ==========================================
# Check API Response
# ==========================================

if response.status_code != 200:

    print("\n❌ Unable to get weather information.")

    if "message" in data:
        print("Reason:", data["message"])

    exit()


# ==========================================
# Extract Weather Data
# ==========================================

city_name = data["name"]
country = data["sys"]["country"]

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]

humidity = data["main"]["humidity"]

pressure = data["main"]["pressure"]

weather = data["weather"][0]["description"]

wind_speed = data["wind"]["speed"]


# ==========================================
# Display Weather
# ==========================================

print("\n======================================")
print("          WEATHER INFORMATION")
print("======================================")

print(f"City          : {city_name}")
print(f"Country       : {country}")
print(f"Temperature   : {temperature} °C")
print(f"Feels Like    : {feels_like} °C")
print(f"Weather       : {weather.title()}")
print(f"Humidity      : {humidity}%")
print(f"Pressure      : {pressure} hPa")
print(f"Wind Speed    : {wind_speed} m/s")

print("======================================")
print("        WEATHER APP COMPLETED")
print("======================================")