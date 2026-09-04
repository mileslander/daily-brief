import requests
import xml.etree.ElementTree as ET
import datetime
from datetime import timedelta
from zoneinfo import ZoneInfo
import os
import os.path
import sys
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def parser():
    print("Getting Todays News")
    urls = ["https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml", "https://feeds.bbci.co.uk/sport/tennis/rss.xml"]
    now = datetime.datetime.now(ZoneInfo("America/Edmonton"))
    today = now.date()
    yesterday = (now - timedelta(days=1)).date()

    for url in urls:
      response = requests.get(url)
      tree = ET.fromstring(response.content)
      items = tree.findall("./channel/item")

      for item in items:
          pubdate= item.find("pubDate")
          if pubdate is not None:
              if url == "https://feeds.bbci.co.uk/sport/tennis/rss.xml":
                 pubdate = pubdate.text.replace(" GMT", " +0000")
                 pub_date = datetime.datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")
              else:
                pub_date = datetime.datetime.strptime(pubdate.text, "%a, %d %b %Y %H:%M:%S %z")
              if pub_date.date() in [yesterday, today]:
                  description = item.find("description")
                  print(description.text)
      
    return

def calendar():
  SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
  
  creds = Credentials.from_service_account_file("service-account.json", scopes=SCOPES)

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    mountain_time = ZoneInfo("America/Edmonton")
    today = datetime.datetime.now(mountain_time).date()
    start_of_day = datetime.datetime(today.year, today.month, today.day, tzinfo=mountain_time).isoformat()
    end_of_day = datetime.datetime(today.year, today.month, today.day, 23, 59, 59, tzinfo=mountain_time).isoformat()


    print("Getting Todays Events")
    events_result = (
        service.events()
        .list(
            calendarId="mlander@ualberta.ca",
            timeMin=start_of_day,
            timeMax=end_of_day,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start, event["summary"])

  except HttpError as error:
    print(f"An error occurred: {error}")
  except TimeoutError as error:
    print(f"Calendar API timeout: {error}")
  except Exception as error:
    print(f"Calendar error: {error}")

def hackernews():
    print("Getting Hacker News")
    response = requests.get("https://news.ycombinator.com/rss")
    if response.ok:
        tree = ET.fromstring(response.content)
        items = tree.findall("./channel/item/title")
        for item in items:
            print(item.text)

def weather():
    print("Getting Todays Weather")
    BASE = "http://api.weatherapi.com/v1"
    weather_api = os.getenv("WEATHER_API")
    method = "/current.json?key=" + weather_api + "&q=Edmonton"
    url = BASE + method
    response = requests.get(url)
    print(response.content)
    return

def main():
    parser()
    hackernews()
    weather()
    calendar()

if __name__ == "__main__":
    main()
