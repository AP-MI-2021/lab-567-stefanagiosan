from Logic.CRUD import adaugaCheltuiala
from Tests.testAll import runAllTests
from UI.console import runMenu

def main():
    runAllTests()
    lista = []
    lista = adaugaCheltuiala(1, 1, 100, "12.3.2000", "canal", lista)
    lista = adaugaCheltuiala(2, 2, 300, "10.4.2012", "intretinere", lista)
    lista = adaugaCheltuiala(3, 3, 450, "10.4.2018", "canal", lista)
    lista = adaugaCheltuiala(4, 4, 600, "10.4.2016", "intretinere", lista)
    lista = adaugaCheltuiala(5, 5, 250, "10.4.2020", "alte cheltuieli", lista)

    runMenu(lista)

main()

