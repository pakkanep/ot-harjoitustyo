import threading
from services.infoseeker import InfoSeeker


class Operations(InfoSeeker):
    def __init__(self):
        super().__init__()

    def save_results(self):
        print("save_results testitulostus")

    def get_results(self):
        print("get_results testitulostus")

    def multi_thread(self, url, task, amount):
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

    def handle_links(self, seen, url=None):
        for link in self.links:
            if self.interruptvalue:
                break
            if link in seen:
                continue
            seen.add(link)
            self.handle(link)

    def start_query(self):
        self.reset_all()
        try:
            url = "https://duunitori.fi/tyopaikat/ala/ohjelmointi-ja-ohjelmistokehitys?sivu="
            self.multi_thread(url, self.seek_all_pages, 3)
            print("Linkit haettu")
            self.multi_thread(url, self.handle_links, 6)
            print("Haku suoritettu")
        except KeyboardInterrupt:
            self.interruptvalue = True
            print("Haku keskeytetty")
