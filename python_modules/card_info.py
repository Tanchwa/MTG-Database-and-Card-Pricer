
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from mtgsdk import Card, Set


def multiverse_lookup(multiverse_id):
    card_info = Card.find(multiverse_id)
    card_name = card_info.name
    set_name = card_info.set_name
    return card_name, set_name


#this needs to be changed to make beginings of names capitals

def card_price_lookup(card_name, set_name):
    if "," or " " in set_name or card_name:
        card_name = card_name.replace(" ","+")
        set_name = set_name.replace(" ","+")
        card_name = card_name.replace(" ","+")
        set_name = set_name.replace(",","+")
        card_name = card_name.replace(",","+")
    if "'" in set_name or card_name:
        set_name = set_name.replace("'","")
        card_name = card_name.replace("'","")
    card_price_url = "https://www.mtggoldfish.com/price/{}/{}#paper".format(set_name,card_name)
    uClient = uReq(card_price_url)
    card_price_html = uClient.read()
    uClient.close()
    page_soup = soup(card_price_html, "html.parser")
    card_price_tag = page_soup.find("div",{"class":"price-box-price"})
    card_price_string = str(card_price_tag)
    #to index length of the value, find total length of string then - nonsense (37 characters)
    length_price = len(card_price_string) - 37
    card_price = "$" + card_price_string[31:31+length_price]
    return card_price
    

if __name__ == "__main__":
    pass

def test_script(multiverse_id):
    card_name, set_name = multiverse_lookup(multiverse_id)
    card_price = card_price_lookup(card_name, set_name)
    print(card_name + " from " +set_name + " is " + card_price)

multiverse_ids = [1135, 1, 2303, 74324, 525598, 10422]
for multiverse_id in multiverse_ids:
    test_script(multiverse_id)
