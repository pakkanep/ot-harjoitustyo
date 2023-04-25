from bs4 import BeautifulSoup
import requests


class InfoSeeker:
    def __init__(self):
        self.successful_add_handles = 0
        self.failed_add_handles = 0
        self.successful_page_handles = 0
        self.amount_pages = 0
        self.amount_ads = 0
        self.seeking = 0
        self.information_dict = {
            "Java": 1,
            "Python": 1,
            "C++": 1,
            "Go": 1,
            "Rust": 1,
            "Javascript": 1,
            "PHP": 1,
            "C#": 1,
            "Ruby": 1,
            "C": 1,
            "SQL": 1,
            "PostgreSQL": 1,
            "TypeScript": 1,
            "Kotlin": 1,
            "Scala": 1,
            "React": 1,
            "Node.js": 1,
            ".NET": 1
        }

    def reset_all(self):
        self.information_dict = dict.fromkeys(self.information_dict, 1)
        self.amount_ads = 0
        self.amount_pages = 0
        self.successful_page_handles = 0
        self.successful_add_handles = 0
        print("Hakutiedot resetoitu")


    def search_links(self, url):
        try:    
            result = requests.get(url, timeout=(10, 10))
            doc = BeautifulSoup(result.text, "html.parser")
            for link in doc.find_all(class_="job-box__hover gtm-search-result"):
                site_url = "https://duunitori.fi"+link.get('href')
                self.handle(site_url)

        except (TimeoutError, ValueError, IndexError, AttributeError):
            print("Ongelma linkkien haussa")

    def search_amount_of_ads(self, url):
        try:
            result = requests.get(url, timeout=(20, 20))
            doc = BeautifulSoup(result.text, "html.parser")
            tags = (doc.find_all(
                class_="m-b-10-on-all text--body text--left text--center-desk"))
            return int(tags[0].b.text)

        except (TimeoutError, ValueError, IndexError, AttributeError):
            print("Ongelma hakemuksien määrän hakemisessa")
            return None

    def search_amount_of_pages(self, url):
        try:
            result = requests.get(url, timeout=(20, 20))
            doc = BeautifulSoup(result.text, "html.parser")
            tags = doc.find_all(class_="pagination__pagenum")
            amount = int(tags[-1].text)
            return amount

        except (TimeoutError, ValueError, IndexError, AttributeError):
            print("Ongelma sivujen määrän hakemisessa")
            return None

    def seek_all_pages(self, url):
        self.amount_pages = self.search_amount_of_pages(url)
        self.amount_ads = self.search_amount_of_ads(url)
        for pagenum in range(1, self.amount_pages+1):
            self.search_links(url+str(pagenum))
            self.successful_page_handles += 1

    def handle(self, url):
        try:
            result = requests.get(url, timeout=(20,20))
            doc = BeautifulSoup(result.text, "html.parser")
            tags = doc.find_all(class_="description-box")
            description = tags[0].text
            self.search_instances(description)
            self.successful_add_handles += 1
            print(
                f"Sivuja käsitelty: {self.successful_page_handles}/{self.amount_pages} \
                Ilmoituksia käsitelty: {self.successful_add_handles}/{self.amount_ads}")

        except (TimeoutError, ValueError, IndexError, AttributeError):
            self.failed_add_handles += 1
            print("Ongelma sivun Käsittelyssä")

    def search_instances(self, text: str):
        check_dict = {
            "Java": 0,
            "Python": 0,
            "C++": 0,
            "Go": 0,
            "Rust": 0,
            "Javascript": 0,
            "PHP": 0,
            "C#": 0,
            "Ruby": 0,
            "C": 0,
            "SQL": 0,
            "PostgreSQL": 0,
            "TypeScript": 0,
            "Kotlin": 0,
            "Scala": 0,
            "React": 0,
            "Node.js": 0,
            ".NET": 0
        }

        for name in self.information_dict:
            validword = name+" "
            if text.find(name) is not None:
                alku = text.find(name)
                if validword == text[alku:alku+len(name)+1] and check_dict[name] == 0:
                    check_dict[name] = 1
                    self.information_dict[name] += 1

    def start(self):
        url = "https://duunitori.fi/tyopaikat/ala/ohjelmointi-ja-ohjelmistokehitys?sivu="
        self.seek_all_pages(url)
