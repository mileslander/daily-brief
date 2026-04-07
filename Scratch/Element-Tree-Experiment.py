import requests
#https://pypi.org/project/requests/

import xml.etree.ElementTree as ET
#https://docs.python.org/3/library/xml.etree.elementtree.html

#Prints all text
def XML_Loops(url):
    response = requests.get(url)
    tree = ET.fromstring(response.content)
    for branches in tree:
        for branch in branches:
            for leaf in branch:
                print(leaf.text)
    print("End Loops")
    return

#Prints only article descriptions
def XML_Findall(url):
    response = requests.get(url)
    tree = ET.fromstring(response.content)
    descriptions = tree.findall("./channel/item/description")
    for description in descriptions:
        print(description.text)
        
    print("End Findall")
    return

#Prints all types of descriptions
def XML_Iterator(url):
    response = requests.get(url)
    tree = ET.fromstring(response.content)
    descriptions = tree.iter("description")
    for description in descriptions:
        print(description.text)
    print("End Iterator")
    return

def XML(url):
    XML_Loops(url)
    XML_Findall(url)
    XML_Iterator(url)
    return

def main():
    XML("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")

if __name__ == "__main__":
    main()
