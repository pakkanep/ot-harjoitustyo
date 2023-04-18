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
        return

    def search_links(self, url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        try:
            for link in doc.find_all(class_="job-box__hover gtm-search-result"):
                site_url = "https://duunitori.fi"+link.get('href')
                self.handle(site_url)

        except ValueError or IndexError or AttributeError:
            print("Ongelma linkkien haussa")
            return

    def search_amount_of_ads(self, url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        try:
            tags = (doc.find_all(class_="m-b-10-on-all text--body text--left text--center-desk"))
            return int(tags[0].b.text)

        except ValueError or IndexError or AttributeError:
            print("Ongelma hakemuksien määrän hakemisessa")
            return

    def search_amount_of_pages(self, url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        try:
            tags = doc.find_all(class_="pagination__pagenum")
            amount = int(tags[-1].text)
            return amount

        except ValueError or IndexError or AttributeError:
            print("Ongelma sivujen määrän hakemisessa")
            return

    def seek_all_pages(self, url):
        self.amount_pages = self.search_amount_of_pages(url)
        self.amount_ads = self.search_amount_of_ads(url)
        for pagenum in range(1, self.amount_pages+1):
            self.search_links(url+str(pagenum))
            self.successful_page_handles += 1
        return

    def handle(self, url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        try:
            tags = doc.find_all(class_="description-box")
            description = tags[0].text
            self.search_instances(description)
            self.successful_add_handles += 1
            print(f"Sivuja käsitelty: {self.successful_page_handles}/{self.amount_pages} Ilmoituksia käsitelty: {self.successful_add_handles}/{self.amount_ads}")

        except ValueError or IndexError or AttributeError:
            self.failed_add_handles += 1
            print("Ongelma sivun Käsittelyssä")
            return

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

        for a, b in self.information_dict.items():
            validword = a+" "
            if text.find(a) is not None:
                alku = text.find(a)
                if validword == text[alku:alku+len(a)+1] and check_dict[a] == 0:
                    check_dict[a] = 1
                    self.information_dict[a] += 1
        
        return

    def start(self):
        self.seeking = 1
        url = "https://duunitori.fi/tyopaikat/ala/ohjelmointi-ja-ohjelmistokehitys?sivu="
        self.seek_all_pages(url)
        self.seeking = 0
        return


"""
if __name__ == "__main__":
    url = "https://duunitori.fi/tyopaikat?haku=fullstack"
    url2 = "https://duunitori.fi/tyopaikat/ala/ohjelmointi-ja-ohjelmistokehitys?sivu="
    url3 = "https://duunitori.fi/tyopaikat/ala/ohjelmointi-ja-ohjelmistokehitys"
    obj = InfoSeeker()
    obj.start()
"""
