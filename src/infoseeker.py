"""The purpose of this module is that it can do a search for available fullstack
developer job-applications on "Duunitori" website and to then find the links 
provided by the search. The links are then passed to the infohandler.py module
"""

from bs4 import BeautifulSoup
from infohandler import InfoHandler
import requests



test = InfoHandler()


def seek(url: str):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    new = doc.find_all(class_="job-box__hover gtm-search-result")
    amount = get_amount(url)
    spot = 0
    information = []
    while True:
        try:
            information.append(parse(new[spot].prettify()))
            print(f"{spot+1}/{amount} haettu")
        except IndexError:
            break
        spot+=1
    return test.info_dict

def seek_one(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    new = doc.find_all(class_="job-box__hover gtm-search-result")
    #indeksi 0 on vain testausta varten!!!!
    return parse(new[0].prettify())

def parse(text: str):
    start = text.find("href=")
    idx = start+6
    while True:
        if text[idx] == '"':
            break
        else:
            idx+=1
    url = "https://duunitori.fi"+text[start+6:idx]
    
    return test.handle(url)

def get_amount(url: str):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    new = doc.find_all(class_="grid-container")
    final = new[2].find(["b"])
    return int(final.text)

def pass_url():
    return seek("https://duunitori.fi/tyopaikat?haku=fullstack")


def is_valid(url: str):
    requests.get()


if __name__ == "__main__":
    url = "https://duunitori.fi/tyopaikat?haku=fullstack"
    is_valid(url)