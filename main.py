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
    lista =[]

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

