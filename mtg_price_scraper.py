
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
set_name = 'Urzas Saga'
card_name = 'Gaeas Cradle'
set_name = set_name.replace(" ","+")
card_name = card_name.replace(" ","+")
#These variables will be changed to match the database schema once implimented#
#create a loop to run this through all cards in database#
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
print(card_price)
#check if card price is the same, if yes redo loop, if no continue to print new value into database

#test to see if code works with other cards
set_name = 'Tempest'
card_name = 'Bottle Gnomes'
#These variables will be changed to match the database schema once implimented#
set_name = set_name.replace(" ","+")
card_name = card_name.replace(" ","+")
#create a loop to run this through all cards in database#
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
print(card_price)
