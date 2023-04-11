from infoseeker import InfoSeeker
from diagramcreator import create

test_object = InfoSeeker()

def execute():
    print("Suorita komento syötämällä ohjelmalle jokin alla olevista numeroista:")
    print("1: Suorita haku")
    print("2: Näytä kaavio hakutuloksista")
    print("3: Lopeta ohjelman suoritus")
    syote = ""
    while True:
        syote = input("Syötä numero: ")
        if syote == "1":
            result = test_object.pass_url()
            print("Haku suoritettu")

        if syote == "2":
            create(result)

        if syote == "3":
            print("Mukavaa päivää!")
            break