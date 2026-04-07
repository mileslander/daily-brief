import requests
import xml.etree.ElementTree as ET

BASE = "http://api.weatherapi.com/v1"
KEY = "8ae4febcd96c4aeaa3c181834260204"

def weather_call(method):
    url = BASE + method
    print(url)
    response = requests.get(url)
    print(response.content)
    return


def main():
    print("Getting Todays Weather")
    weather_call("/current.json?key=" + KEY + "&q=Edmonton")

if __name__ == "__main__":
    main()