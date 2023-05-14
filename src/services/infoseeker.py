from bs4 import BeautifulSoup
import requests
from urllib3 import exceptions


class InfoSeeker:
    """Luokka, joka suorittaa esiintymähaun ja palauttaa sanakirjan,
        joka sisältää kielien esiintymät.

    Attributes:
        successful_add_handles: onnistuneiden työpaikkailmoitusten lkm.
        interruptvalue: keskeyttää tarvittaessa haun suorituksen
        links = set tietorakenne johon linkit tallennetaan
        amount_pages: kertoo sivujen määrän metodin for loopille
        amount_ads: työpaikkailmoitusten lukumäärä yhteensä.
        information_dict: Sanakirja, jonka avaimina olevat arvot ovat ohjelmointikielien nimiä,
        joita etsitään sivuilta.
    """

    def __init__(self):
        """Konstruktori alustaa kaikki tarpeelliset muuttujat ja tietorakenteet,
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
        """Alustaa kaikki muuttujat, jotka ovat ohjelman
            suorituksen aikana muuttuneet.
        """

        self.information_dict = dict.fromkeys(self.information_dict, 1)
        self.interruptvalue = False
        self.links.clear()
        self.amount_ads = 0
        self.amount_pages = 0
        self.successful_add_handles = 0

    def search_links(self, url):
        """Etsii kaikkien ilmoitusten linkit, jotka sivuilta löytyy ja
            lisää ne set tietorakenteeseen.

        Args:
            url: linkki nettisivulle.

        Exceptions:
            mahdollinen ongelma sivun käsittelyssä.
        """
        try:
            result = requests.get(url, timeout=(20, 20))
            doc = BeautifulSoup(result.text, "html.parser")
            for link in doc.find_all(class_="job-box__hover gtm-search-result"):
                if self.interruptvalue:
                    break
                site_url = "https://duunitori.fi"+link.get('href')
                self.links.add(site_url)


        except (requests.exceptions.Timeout,
                IndexError,
                requests.exceptions.ConnectionError,
                exceptions.MaxRetryError,
                exceptions.NewConnectionError,
                exceptions.ResponseError
            ):
            pass

    def search_amount_of_ads(self, url):
        """Etsii annetun linkin avulla löydettyjen työpaikkailmoitusten
            kokonaislukumäärän

        Args:
            url: linkki nettisivulle

        Returns:
            tags muutuujan osan josta tarkka luku löytyy tai
            ongelman sattuessa 0.
        """
        try:
            result = requests.get(url, timeout=(20, 20))
            doc = BeautifulSoup(result.text, "html.parser")
            tags = (doc.find_all(
                class_="m-b-10-on-all text--body text--left text--center-desk"
            ))
            return int(tags[0].b.text)

        except (requests.exceptions.Timeout,
                IndexError,
                requests.exceptions.ConnectionError,
                exceptions.MaxRetryError,
                exceptions.NewConnectionError,
                exceptions.ResponseError
            ):
            return 0

    def search_amount_of_pages(self, url):
        """Etsii parametrina annetun linkin avulla kuinka monelle sivulle
            työpaikkailmoitukset on jaettu. Eli kuinka monta sivua on käytävä läpi,
            että kaikki työpaikkailmoitusten linkit löydetään.

        Args:
            url: linkki nettisivulle

        Returns:
            palauttaa löydettujen sivujen lukumäärän tai
            ongelman sattuessa 0.
        """
        try:
            result = requests.get(url, timeout=(20, 20))
            doc = BeautifulSoup(result.text, "html.parser")
            tags = doc.find_all(class_="pagination__pagenum")
            amount = int(tags[-1].text)
            return amount

        except (requests.exceptions.Timeout,
                IndexError,
                requests.exceptions.ConnectionError,
                exceptions.MaxRetryError,
                exceptions.NewConnectionError,
                exceptions.ResponseError
            ):
            return 0

    def seek_all_pages(self, seen, url):
        """Hakee ensin muuttujaan sivujen määrän for looppia varten
            ja sitten ilmoitusten määrän. Sen jälkeen loopissa kutsutaan
            metodia search_links jossa lisätään kaikki löydetyt linkit set tietorakenteeseen.
            Jokaisella kieroksella käyty sivu lisätään "set" rakenteeseen jonka avulla
            tiedetään että tietty sivu on jo käyty läpi. 
        Args:
            seen: set rakenne joka pitää kirjaa käydyistä sivuista
            url: linkki sivulle
        """

        self.amount_pages = self.search_amount_of_pages(url)
        self.amount_ads = self.search_amount_of_ads(url)
        for pagenum in range(1, self.amount_pages+1):
            if self.interruptvalue:
                break
            if pagenum in seen:
                continue
            seen.add(pagenum)
            self.search_links(url+str(pagenum))

    def handle(self, url):
        """
        Args:
            url: linkki nettisivulle
        """
        try:
            result = requests.get(url, timeout=(20, 20))
            doc = BeautifulSoup(result.text, "html.parser")
            tags = doc.find_all(class_="description-box")
            description = tags[0].text
            self.search_instances(description)
            self.successful_add_handles += 1

        except (requests.exceptions.Timeout,
                IndexError,
                requests.exceptions.ConnectionError,
                exceptions.MaxRetryError,
                exceptions.NewConnectionError,
                exceptions.ResponseError
            ):
            pass

    def search_instances(self, text: str):
        """Etsii tekstistä kaikki esiintymät jotka sanakirjassa ovat avaimena.
        Args:
            text: merkkijono joka on suodatettu sivun html koodista
        """
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
