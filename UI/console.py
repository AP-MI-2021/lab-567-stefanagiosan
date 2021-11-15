from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from Domain.cheltuiala import toString, getSuma
from Logic.functionalitate import adunareCheltuieli, ordonare, CeaMaiMareCheltuialaPentruTip, sumeLunare



def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala pentru un nr dat")
    print("3. Modificare cheltuiala")
    print("4. Adauga o valoare la toate cheltuielile dintr-o data citita")
    print("5. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("6. Ordonarea cheltuielilor descrescător după sumă.")
    print("7. Afișarea sumelor lunare pentru fiecare apartament. ")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare Cheltuieli")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista, undoList, redoList):
    try:
        id = int(input("dati id-ul cheltuielii: "))
        nr = int(input("dati nr-ul: "))
        suma = int(input("dati suma: "))
        data = input("dati data: ")
        tip = input("dati tipul: ")

        rezultat = adaugaCheltuiala(id, nr, suma, data, tip, lista, undoList, redoList)

        return rezultat

    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def uiStergeCheltuiala(lista, undoList, redoList):
    try:
        nr = int(input("dati nr-ul cheltuielii de sters: "))

        rezultat = stergeCheltuiala(nr, lista, undoList, redoList)

        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista


def uiModificaCheltuiala(lista, undoList, redoList):
    try:
        id = int(input("dati id-ul cheltuielii: "))
        nr = int(input("dati nr-ul cheltuielii de modificat: "))
        suma = int(input("dati suma noua: "))
        data = input("dati noua data: ")
        tip = input("dati noul tip: ")


        rezultat = modificaCheltuiala(id, nr, suma, data, tip, lista, undoList, redoList)

        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista



def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiAdunareCheltuiala(lista, undoList, redoList):
    try:
        data = input("dati data pt care cheltuieli li se va adauga o valoarea: ")
        valoarea  = int(input("dati valoarea pe care vreti sa o adaugati: "))
        undoList.append(lista)
        redoList.clear()
        return adunareCheltuieli(data, valoarea, lista )
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista



def uiOrdonare(lista, undoList, redoList):
    lista = ordonare(lista)
    undoList.append(lista)
    redoList.clear()
    print("ordonarea a fost facuta cu succes")
    return lista

def uiCeaMaiMareCheltuialaPentruTip(lista):
    rezultat = CeaMaiMareCheltuialaPentruTip(lista)
    for tip in rezultat:
        print(f'Pentru tipul: {tip} avem cheltuiala: {getSuma(rezultat[tip])}')

def uiSumeLunare(lista):
    rezultat = sumeLunare(lista)
    for luna in rezultat:
        print(f'Pentru luna: {luna} avem lista de sume: {rezultat[luna]}')


def doUndo(lista, undoList, redoList):

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    else:
        print("nu se poate face undo!")
    return lista


def doRedo(lista, undoList, redoList):
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    else:
        print("nu se poate face redo!")
    return lista


def runMenu(lista):
    undoList = []
    redoList = []
    lista = []
    '''lista = adaugaCheltuiala(1, 1, 100, "12.3.2000", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 2, 300, "10.4.2012", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(3, 3, 450, "10.4.2018", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala(4, 4, 600, "10.4.2016", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(5, 5, 250, "10.4.2020", "alte cheltuieli", lista, undoList, redoList)'''

    while True:
        printMenu()
        optiune = input("dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiAdunareCheltuiala(lista, undoList, redoList)
        elif optiune == "5":
            uiCeaMaiMareCheltuialaPentruTip(lista)
        elif optiune == "6":
            lista =  uiOrdonare(lista, undoList, redoList)
        elif optiune == "7":
            uiSumeLunare(lista)
        elif optiune == "u":
            lista = doUndo(lista, undoList, redoList)
            # if len(undo_list) > 0:
                # redo_list.append(lista)
                # lista = undo_list.pop()
            # else:
                # print("Nu se poate face undo!")
        elif optiune == "r":
            lista = doRedo(lista, undoList, redoList)
            # if len(redo_list) > 0:
                # undo_list.append(lista)
                # lista = redo_list.pop()
            # else:
                # print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("optiune gresita!reincercati")