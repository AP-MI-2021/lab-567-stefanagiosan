from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from Domain.cheltuiala import toString
from Logic.functionalitate import adunareCheltuieli

def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala pentru un nr dat")
    print("3. Modificare cheltuiala")
    print("4. Adauga o valoare la toate cheltuielile dintr-o data citita")
    print("a. Afisare Cheltuieli")
    print("x. Iesire")

def uiAdaugaCheltuiala(lista):
    nr = int(input("dati nr-ul: "))
    suma = int(input("dati suma: "))
    data = input("dati data: ")
    tip = input("dati data: ")
    return adaugaCheltuiala(nr, suma, data, tip, lista)

def uiStergeCheltuiala(lista):
    nr = input("dati nr-ul cheltuielii de sters: ")
    return stergeCheltuiala(nr, lista)

def uiModificaCheltuiala(lista):
    nr = int(input("dati nr-ul cheltuielii de modificat: "))
    suma = int(input("dati suma noua: "))
    data = input("dati noua data: ")
    tip = input("dati noul tip: ")
    return modificaCheltuiala(nr, suma, data, tip, lista)

def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiAdunareCheltuiala(lista):
    data = input("dati data pt care cheltuieli li se va adauga o valoarea: ")
    valoarea  = int(input("dati valoarea pe care vreti sa o adaugati: "))
    return adunareCheltuieli(data, valoarea, lista )




def runMenu(lista):
    lista = []
    while True:
        printMenu()
        optiune = input("dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista)
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista)
        elif optiune == "4":
            lista = uiAdaugaCheltuiala(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("optiune gresita!reincarcati")