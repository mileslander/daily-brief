import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def parser(url):
    response = requests.get(url)
    tree = ET.fromstring(response.content)
    items = tree.findall("./channel/item")
    for item in items:
        pubdate = item.find("pubDate")
        if pubdate is not None:
            pub_date = datetime.strptime(pubdate.text, "%a, %d %b %Y %H:%M:%S %z")
            today = datetime.now().date()
            yesterday = (datetime.now() - timedelta(days=1)).date()
            if pub_date.date() in [yesterday, today]:
                description = item.find("description")
                print(description.text)
        

def main():
    print("Getting Todays News")
    parser("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    parser("https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml")
    parser("https://rss.nytimes.com/services/xml/rss/nyt/Tennis.xml")
    parser("https://rss.nytimes.com/services/xml/rss/nyt/Health.xml")
    parser("https://feeds.bbci.co.uk/sport/tennis/rss.xml")

if __name__ == "__main__":
    main()