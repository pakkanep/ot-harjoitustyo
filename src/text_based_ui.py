from infoseeker import pass_url
from diagramcreator import create

def suorita():
    print("Suorita komento syötämällä ohjelmalle jokin alla olevista numeroista:")
    print("1: Suorita haku")
    print("2: Näytä kaavio hakutuloksista")
    print("3: Lopeta ohjelman suoritus")
    syote = ""
    while True:
        syote = input("Syötä numero: ")
        if syote == "1":
            result = pass_url()
            print("Haku suoritettu")

        if syote == "2":
            create(result)

        if syote == "3":
            print("Mukavaa päivää!")
            break