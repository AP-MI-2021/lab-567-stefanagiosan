from Tests.testAll import runAllTests
from UI.console import runMenu
from Logic.CRUD import adaugaCheltuiala

def main():
    runAllTests()
    lista = []
    lista = adaugaCheltuiala(1, 100, "12.03.2010", "canal")
    lista = adaugaCheltuiala(2, 400, "20.11.2020", "intretinere")
    runMenu(lista)

main()

