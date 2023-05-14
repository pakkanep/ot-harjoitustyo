import threading
from services.infoseeker import InfoSeeker


class Operations(InfoSeeker):
    """Perii luokan InfoSeeker ja pääasiallisena tarkoituksena
        monisäikeistys
    """
    def __init__(self):
        super().__init__()

    def multi_thread(self, url, task, amount):
        """Monisäikeistää halutut tehtävät

        Args:
            url: linkki nettisivulle
            task: mikä funktio halutaan suoritukseen
            amount: säikeiden määrä
        """
        daemon_value = False
        seen = set()
        threads = []
        for _ in range(amount):
            if self.interruptvalue:
                break
            thread = threading.Thread(
                target=task,
                daemon=daemon_value,
                args=(seen, url)
            )
            thread.start()
            threads.append(thread)
            daemon_value = True

        for thread in threads:
            if self.interruptvalue:
                break
            thread.join()

    def handle_links(self, seen, url): # pylint: disable=unused-argument
        """Käy loopissa läpi kaikki työpaikkailmoitukset

        Args:
            seen: pitää kirjaa siitä mitkä linkit on käyty läpi 
        """
        for link in self.links:
            if self.interruptvalue:
                break
            if link in seen:
                continue
            seen.add(link)
            self.handle(link)

    def start_query(self):
        """Aloittaa haun, resetoimalla kaikki arvot ja kutsuu
            multithread funktiota joka hakee eka linkit,
            jonka jälkeen työpaikkailmoitukset käydään läpi

        Args:
            url: linkki duunitorin sivuille
            interruptvalue: boolean joka kertoo jos haku halutaan keskyettää
        """
        self.reset_all()
        try:
            url = "https://duunitori.fi/tyopaikat/ala/ohjelmointi-ja-ohjelmistokehitys?sivu="
            self.multi_thread(url, self.seek_all_pages, 3)
            self.multi_thread(url, self.handle_links, 6)
        except KeyboardInterrupt:
            self.interruptvalue = True
