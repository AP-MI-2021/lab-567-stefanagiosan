from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from Domain.cheltuiala import toString, getTip, getSuma
from Logic.functionalitate import adunareCheltuieli, ordonare, CeaMaiMareCheltuialaPentruTip, sumeLunare
from Tests.testCRUD import CheltuieliPentruTeste


def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala pentru un nr dat")
    print("3. Modificare cheltuiala")
    print("4. Adauga o valoare la toate cheltuielile dintr-o data citita")
    print("5. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("6. Ordonarea cheltuielilor descrescător după sumă.")
    print("7. Afișarea sumelor lunare pentru fiecare apartament. ")
    print("a. Afisare Cheltuieli")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista):
    id = int(input("dati id-ul cheltuielii: "))
    nr = int(input("dati nr-ul: "))
    suma = int(input("dati suma: "))
    data = input("dati data: ")
    tip = input("dati data: ")
    return adaugaCheltuiala(id, nr, suma, data, tip, lista)


def uiStergeCheltuiala(lista):
    nr = input("dati nr-ul cheltuielii de sters: ")
    return stergeCheltuiala(nr, lista)


def uiModificaCheltuiala(lista):
    id = int(input("dati id-ul cheltuielii: "))
    nr = int(input("dati nr-ul cheltuielii de modificat: "))
    suma = int(input("dati suma noua: "))
    data = input("dati noua data: ")
    tip = input("dati noul tip: ")
    return modificaCheltuiala(id, nr, suma, data, tip, lista)


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiAdunareCheltuiala(lista):
    data = input("dati data pt care cheltuieli li se va adauga o valoarea: ")
    valoarea  = int(input("dati valoarea pe care vreti sa o adaugati: "))
    return adunareCheltuieli(data, valoarea, lista )


def uiOrdonare(lista):
    lista = ordonare(lista)
    print("ordonarea a fost facuta cu succes")
    return lista

def uiCeaMaiMareCheltuialaPentruTip(lista):
    rezultat = CeaMaiMareCheltuialaPentruTip(lista)
    for tip in rezultat:
        print(f'Pentru tipul: {tip} avem cheltuiala: {getSuma(rezultat[tip])}')

def uiSumeLunare(lista):
    rezultat = sumeLunare(lista)
    for tip in rezultat:
        print(f'Pentru tipul: {tip} avem cheltuiala: {getSuma(rezultat[tip])}')


def runMenu(lista):
    lista = CheltuieliPentruTeste()
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
        elif optiune == "5":
            uiCeaMaiMareCheltuialaPentruTip(lista)
        elif optiune == "6":
            lista =  uiOrdonare(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("optiune gresita!reincarcati")