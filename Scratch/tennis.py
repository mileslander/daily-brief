import requests
import xml.etree.cElementTree as ET
from datetime import datetime, timedelta

def request():
    today = datetime.now().date()
    yesterday = (datetime.now() - timedelta(days=1)).date()

    response = requests.get("https://feeds.bbci.co.uk/sport/tennis/rss.xml")
    tree = ET.fromstring(response.content)
    items = tree.findall("./channel/item")
    for item in items:
        pubdate = item.find("pubDate")
        if pubdate is not None:
            date_str = pubdate.text.replace(" GMT", " +0000")
            pub_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
            if pub_date.date() in [today, yesterday]:
                description = item.find("description")
                print(description.text)
    return

if __name__ == "__main__":
    request()