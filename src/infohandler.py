# The goal for this module is to handle the search result data provided by 
# "InfoSeeker" module, meaning that this scrapes the sites and counts the
# instances of different required programming language names. The dictionary is 
# harcoded by default, but maybe the user can search the instances of just the 
# languages that he or she are interested of.
from bs4 import BeautifulSoup
import requests

class InfoHandler:
    def __init__(self):
        self.info_dict = {
        "Java": 0,
        "Python" : 0,
        "Cpp": 0,
        "Go": 0,
        "Rust": 0,
        "Javascript": 0,
        "PHP": 0,
        "C#": 0,
        "Ruby": 0,
        "C": 0,
        "SQL": 0,
        "TypeScript": 0,
        "Kotlin": 0,
        "Scala": 0,
        "React": 0,
        "Node.js": 0
        }

    def handle(self, url: str):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        tags = doc.find_all(["div"], "gtm-apply-clicks description description--jobentry")
        info = self.search_instances(tags[0].prettify())
        self.save_instances(info)


    def search_instances(self, text: str):
        default_dict = {
            "Java": 0,
            "Python" : 0,
            "Cpp": 0,
            "Go": 0,
            "Rust": 0,
            "Javascript": 0,
            "PHP": 0,
            "C#": 0,
            "Ruby": 0,
            "C": 0,
            "SQL": 0,
            "TypeScript": 0,
            "Kotlin": 0,
            "Scala": 0,
            "React": 0,
            "Node.js": 0
        }
        for a, b in default_dict.items():
            if text.find(a) != None:
                alku = text.find(a)

                if a == text[alku:alku+len(a)] and b == 0:
                    default_dict[a]+=1
        
        return default_dict

    def save_instances(self, langs: dict):
        for a, b in self.info_dict.items():
            self.info_dict[a]+=langs[a]


"""
if __name__ == "__main__":
    print(handle("https://duuuunitori.fi/tyopaikat/tyo/fullstack-dev-react-nodejs-aws-sss-r-159458391"))
"""