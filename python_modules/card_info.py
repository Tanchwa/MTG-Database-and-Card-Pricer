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
    bad_characters = {"'", ','}
    uncapitalized_words = {"Of", "For", "A", "The", "In", "An"}
    #check if the bad characters are there and replace all of them
    for bad_character in card_name:
        if bad_character in bad_characters:
            card_name = card_name.replace(bad_character,"")
    for bad_character in set_name:
        if bad_character in bad_characters:
            set_name = set_name.replace(bad_character,"")
    card_name = card_name.title()
    set_name = set_name.title()    
    def make_element_lowercase(list, word):
        word_index = list.index(word)
        list[word_index] = str.lower(list[word_index])
    card_name = card_name.split(" ")
    set_name = set_name.split(" ")
    #check and change the unimportant words to non-capitals
    for unapitalized_word in card_name:
        if unapitalized_word in uncapitalized_words:
            make_element_lowercase(card_name, unapitalized_word)
    for unapitalized_word in set_name:
        if unapitalized_word in uncapitalized_words:
            make_element_lowercase(set_name, unapitalized_word)
    card_name = "+".join(card_name)
    set_name = "+".join(set_name)
    card_price_url = f"https://www.mtggoldfish.com/price/{set_name}/{card_name}#paper"
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
    def test_script(multiverse_id):
        card_name, set_name = multiverse_lookup(multiverse_id)
        card_price = card_price_lookup(card_name, set_name)
        print(card_name + " from " +set_name + " is " + card_price)

    multiverse_ids = [1135, 1, 2303, 74324, 525598, 10422]
    for multiverse_id in multiverse_ids:
        test_script(multiverse_id)




