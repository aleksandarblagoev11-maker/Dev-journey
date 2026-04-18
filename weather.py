import requests

city = input("Enter a city: ")

url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
geo = requests.get(url).json()

if "results" not in geo:
    print(f"Could not find {city}")
else:
    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]
    name = geo["results"][0]["name"]
    country = geo["results"][0]["country"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,relative_humidity_2m"
    weather = requests.get(weather_url).json()

    temp = weather["current"]["temperature_2m"]
    wind = weather["current"]["wind_speed_10m"]
    hum  = weather["current"]["relative_humidity_2m"]

    print(f"\nWeather for {name}, {country}:")
    print(f"  Temperature: {temp}°C")
    print(f"  Wind speed:  {wind} km/h")
    print(f"  Humidity:    {hum} %")