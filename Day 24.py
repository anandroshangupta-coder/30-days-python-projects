# ==========================================
# Day 24 - Weather Data Analyzer
# 30 Days Python GitHub Project Challenge
# ==========================================

import requests


print("======================================")
print("        WEATHER DATA ANALYZER")
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
# API Parameters
# ==========================================

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}


# ==========================================
# Get Weather Data
# ==========================================

try:

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10
    )

    data = response.json()

except requests.exceptions.RequestException:
    print("\n❌ Internet connection error.")
    exit()


# ==========================================
# Check Response
# ==========================================

if response.status_code != 200:

    print("\n❌ Unable to retrieve weather data.")

    if "message" in data:
        print("Reason:", data["message"])

    exit()


# ==========================================
# Extract JSON Data
# ==========================================

city_name = data["name"]
country = data["sys"]["country"]

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]

minimum_temp = data["main"]["temp_min"]
maximum_temp = data["main"]["temp_max"]

humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]

weather = data["weather"][0]["description"]

wind_speed = data["wind"]["speed"]


# ==========================================
# Weather Analysis
# ==========================================

if temperature >= 35:
    temperature_status = "Very Hot 🔥"

elif temperature >= 30:
    temperature_status = "Hot ☀️"

elif temperature >= 20:
    temperature_status = "Pleasant 😊"

elif temperature >= 10:
    temperature_status = "Cool 🌤️"

else:
    temperature_status = "Cold ❄️"


if humidity >= 80:
    humidity_status = "Very Humid"

elif humidity >= 60:
    humidity_status = "Humid"

elif humidity >= 40:
    humidity_status = "Normal"

else:
    humidity_status = "Dry"


# ==========================================
# Display Results
# ==========================================

print("\n======================================")
print("         WEATHER INFORMATION")
print("======================================")

print(f"City             : {city_name}")
print(f"Country          : {country}")

print("--------------------------------------")

print(f"Temperature      : {temperature} °C")
print(f"Feels Like       : {feels_like} °C")
print(f"Minimum Temp     : {minimum_temp} °C")
print(f"Maximum Temp     : {maximum_temp} °C")

print("--------------------------------------")

print(f"Weather          : {weather.title()}")
print(f"Humidity         : {humidity}%")
print(f"Pressure         : {pressure} hPa")
print(f"Wind Speed       : {wind_speed} m/s")

print("--------------------------------------")

print(f"Temperature Status: {temperature_status}")
print(f"Humidity Status   : {humidity_status}")

print("======================================")
print("       ANALYSIS COMPLETED")
print("======================================")