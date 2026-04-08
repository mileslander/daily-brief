import os
import requests

def exp():
    weather_api = os.getenv("WEATHER_API")
    method = "/current.json?key=" + weather_api + "&q=Edmonton"
    BASE = "http://api.weatherapi.com/v1"
    url = BASE + method
    response = requests.get(url)
    print(response.content)

if __name__ == "__main__":
    exp()