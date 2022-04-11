import requests
from bs4 import BeautifulSoup
import json


def fetch_card_html():
    r = requests.get("https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38")
    if r.status_code == 200:
        # if the request is successful return the HTML content
        return r.text
    else:
        # throw an exception if an error occurred
        raise Exception("an error occurred while fetching videocard html")


def get_price(elem):
    price =""
    if elem.find("li", {"class": "price-current"}).find("strong"):
        price+="$"
        price+=elem.find("li", {"class": "price-current"}).find("strong").text.strip()
        price+=elem.find("li", {"class": "price-current"}).find("sup").text.strip()
        return price
    else:
        return "Out of Stock"





def extract_card_info(html):
    # parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    # find all the card elements
    container = soup.findAll("div", {"class": "item-container"})

    # iterate through our  elements
    cards = []
    for card in container:
        # extract the information needed using our observations
        rter=card.find("i", {"class": "rating"})["aria-label"]
        strg=rter.replace("rated","Calificación: ").replace("out of","sobre")
        finder=card.find("a", {"class": "item-title"},href=True)
        cards.append({
            "image": card.find("img")["src"],
            "name": card.find("a", {"class": "item-title"}).text.strip(),
            "rating":strg,
            "link":finder['href'],
            "price": get_price(card),
            

        })

    return cards


# fetch  HTML content
html = fetch_card_html()

# extract our data from the HTML document
cards = extract_card_info(html)

# display the scraper results
for card in cards:
    print(card, "\n")


# save the results locally in JSON
def saveToJson(cards):
    with open("cards.json", "w") as f:
        f.write(json.dumps(cards, indent=2))