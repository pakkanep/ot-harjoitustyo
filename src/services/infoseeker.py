from bs4 import BeautifulSoup
import requests
from requests.exceptions import Timeout, ConnectionError


class InfoSeeker:
    """Luokka, joka suorittaa esiintymähaun ja palauttaa sanakirjan,
        joka sisältää kielien esiintymät.

    Attributes:
        successful_add_handles: onnistuneiden työpaikkailmoitusten lkm.
        failed_add_handles: epäonnistuneiden työpaikkailmoitusten lkm.
        successful_page_handles: onnistuneiden sivujen käsittelyt, josta linkit löytyvät
        amount_ads: työpaikkailmoitusten lukumäärä yhteensä.
        information_dict: Sanakirja, jonka avaimina olevat arvot ovat ohjelmointikielien nimiä,
        joita etsitään sivuilta.
    """

    def __init__(self):
        """Konstruktori alustaa kaikki tarpeelliset muuttujat ja sanakirjan,
            johon halutut esiintymät tallennetaan"""
        self.successful_add_handles = 0
        self.interruptvalue = False
        self.links = set()
        self.amount_pages = 0
        self.amount_ads = 0
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
        """Alustaa kaikki tarvittaessa muuttujat, jotka ovat ohjelman
            suorituksen aikana muuttuneet.
        Args:
            samat kun ylempänä lueteltu
        """
        self.information_dict = dict.fromkeys(self.information_dict, 1)
        self.interruptvalue = False
        self.links.clear()
        self.amount_ads = 0
        self.amount_pages = 0
        self.successful_add_handles = 0
        print("Hakutiedot alustettu")

    def search_links(self, url):
        """Etsii kaikkien ilmoitusten linkit, jotka sivuilta löytyy ja
            lisää ne set tietorakenteeseen

        Args:
            url: linkki nettisivulle
            result: requests.get tallentaa linkistä löytyvän nettisivun html koodin.
            doc: BeautifulSoupin avulla saadaan sisältö läpikäytävään muotoon.
            site_url: doc muuttujan sisällöstä löydetty työpaikkailmoitukseen
            johtava linkki.

        Exceptions:
            mahdollinen ongelma sivun käsittelyssä
        """
        try:
            result = requests.get(url, timeout=(20, 20))
            doc = BeautifulSoup(result.text, "html.parser")
            for link in doc.find_all(class_="job-box__hover gtm-search-result"):
                if self.interruptvalue:
                    break
                site_url = "https://duunitori.fi"+link.get('href')
                self.links.add(site_url)
                print(f"Linkkejä haettu: {len(self.links)}/{self.amount_ads}")

        except (Timeout, IndexError, ConnectionError):
            if ConnectionError:
                print("Nettiyhteys puuttuu!")
            else:
                print("Ongelma linkkien haussa")

    def search_amount_of_ads(self, url):
        """Etsii annetun linkin avulla löydettyjen työpaikkailmoitusten
            kokonaislukumäärän

        Args:
            url: linkki nettisivulle
            result: requests.get tallentaa linkistä löytyvän nettisivun html koodin
            doc: BeautifulSoupin avulla saadaan sisältö läpikäytävään muotoon.
            tags: ilmoitusten lukumäärä etsitty html koodista.

        Returns:
            tags muutuujan osan josta tarkka luku löytyy tai
            ongelman sattuessa 0.

        Exceptions:
            mahdollinen ongelma sivun käsittelyssä.
        """
        try:
            result = requests.get(url, timeout=(20, 20))
            doc = BeautifulSoup(result.text, "html.parser")
            tags = (doc.find_all(
                class_="m-b-10-on-all text--body text--left text--center-desk"
            ))
            return int(tags[0].b.text)

        except (Timeout, IndexError, ConnectionError):
            if ConnectionError:
                print("Nettiyhteys puuttuu!")
            else:
                print("Ongelma hakemuksien määrän hakemisessa")
            return 0

    def search_amount_of_pages(self, url):
        """Etsii parametrina annetun linkin avulla kuinka monelle sivulle
            työpaikkailmoitukset on jaettu. Eli kuinka monta sivua on käytävä läpi,
            että kaikki työpaikkailmoitusten linkit löydetään.

        Args:
            url: linkki nettisivulle
            result: requests.get tallentaa linkistä löytyvän nettisivun html koodin.
            doc: BeautifulSoupin avulla saadaan sisältö läpikäytävään muotoon.
            tags: sivujen lukumäärä etsitty html koodista.
            amount: sivujen tarkka lukumäärä tallennettu.

        Returns:
            palauttaa löydettujen sivujen lukumäärän tai
            ongelman sattuessa 0.

        Exceptions:
            mahdollinen ongelma sivujen lukumäärää etsiessä.
        """
        try:
            result = requests.get(url, timeout=(20, 20))
            doc = BeautifulSoup(result.text, "html.parser")
            tags = doc.find_all(class_="pagination__pagenum")
            amount = int(tags[-1].text)
            return amount

        except (Timeout, IndexError, ConnectionError):
            if ConnectionError:
                print("Nettiyhteys puuttuu!")
            else:
                print("Ongelma sivujen määrän hakemisessa")
            return 0

    def seek_all_pages(self, seen, url):
        self.amount_pages = self.search_amount_of_pages(url)
        self.amount_ads = self.search_amount_of_ads(url)
        for pagenum in range(1, self.amount_pages+1):
            if self.interruptvalue:
                break
            if pagenum in seen:
                continue
            else:
                seen.add(pagenum)
                self.search_links(url+str(pagenum))

    def handle(self, url):
        try:
            result = requests.get(url, timeout=(20, 20))
            doc = BeautifulSoup(result.text, "html.parser")
            tags = doc.find_all(class_="description-box")
            description = tags[0].text
            self.search_instances(description)
            self.successful_add_handles += 1

        except (Timeout, IndexError, ConnectionError):
            if ConnectionError:
                print("Nettiyhteys puuttuu!")
            else:
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
            if self.interruptvalue:
                break
            validword = name+" "
            if text.find(name) is not None:
                alku = text.find(name)
                if validword == text[alku:alku+len(name)+1] and check_dict[name] == 0:
                    check_dict[name] = 1
                    self.information_dict[name] += 1
