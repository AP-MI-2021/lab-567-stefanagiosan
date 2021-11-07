from Logic.CRUD import adaugaCheltuiala
from Tests.testAll import runAllTests
from UI.consolaNoua import runNewMenu
from UI.console import runMenu

def meniuri():
    print("1. Meniul vechi")
    print("2. Meniul nou")
    print("x. iesire")

def main():

    runAllTests()
    lista = []
    lista = adaugaCheltuiala(1, 1, 100, "12.3.2000", "canal", lista)
    lista = adaugaCheltuiala(2, 2, 300, "10.4.2012", "intretinere", lista)
    lista = adaugaCheltuiala(3, 3, 450, "10.4.2018", "canal", lista)
    lista = adaugaCheltuiala(4, 4, 600, "10.4.2016", "intretinere", lista)
    lista = adaugaCheltuiala(5, 5, 250, "10.4.2020", "alte cheltuieli", lista)

    while True:
        meniuri()
        optiune = input("dati optiunea: ")
        if optiune == "1":
            runMenu(lista)
        elif optiune == "2":
            runNewMenu(lista)
        elif optiune == "x":
            break
        else:
            print("optiune gresita! reincercati")




main()

