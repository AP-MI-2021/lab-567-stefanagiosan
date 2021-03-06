from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala


def help():
    print("Instructiuni: Pentru crearea unei cheltuieli trebuie citite id-ul (nr intreg) , numarul apt. (nr intreg) , suma (nr intreg) , data si tipul cheltuielii ")
    print("Comenzile trebuie apelate pe o linie ,separate prin ' ; ' iar campurile prin ' , '  ")
    print("Sa nu se foloseasca alti separatori!")
    print(" add- adauga in lista o cheltuiala noua ,cu valori adecvate ")
    print(" delete- sterge o cheltuiala,introducandu-se cu virgula dupa si numarul cheltuielii,acesta trebuie sa existe")
    print(" showall- afiseaza toate cheltuielile din lista ")
    print(" iesire- daca doriti sa iesiti din meniu")



def add(id, nr, suma, data, tip, lista, undoList, redoList):

    try:
        lista = adaugaCheltuiala(id, nr, suma, data, tip, lista, undoList, redoList)
    except ValueError as ve:
        print("Eroare: ", ve)
    print("cheltuiala a fost adaugata")
    return lista

def delete(nr, lista, undoList, redoList):

    try:
        lista = stergeCheltuiala(nr, lista , undoList, redoList)
    except ValueError as ve:
        print("Eroare: ", ve)
    print("stergerea a fost facuta")
    return lista

def showall(lista):

    for cheltuiala in lista:
        print(toString(cheltuiala))

def modify(id, nr, suma, data, tip, lista, undoList, redoList):

    try:
        lista = modificaCheltuiala(id, nr, suma, data, tip, lista , undoList, redoList)
    except ValueError as ve:
        print("Eroare: ", ve)
    print("modificarea a fost facuta")
    return lista


def runNewMenu(lista):
    undoList = []
    redoList = []
    quit = False
    print("daca aveti nevoie de ajutor scrieti 'help' ")
    while not quit:
        optiune = input("dati comenzile: ")
        optiuni = optiune.split(';')
        for comenzi in optiuni:
            sir = comenzi.split(',')
            if sir[0] == "help":
                help()
            if sir[0] == "add":
                id = int(sir[1])
                nr = int(sir[2])
                suma = int(sir[3])
                data = sir[4]
                tip = sir[5]
                lista = add(id, nr, suma, data, tip, lista, undoList, redoList)
            if sir[0] == "delete":
                nr = int(sir[1])
                lista = delete(nr, lista, undoList, redoList)
            if sir[0] == "showall":
                showall(lista)
            if sir[0] == "modify":
                id = int(sir[1])
                nr = int(sir[2])
                suma = int(sir[3])
                data = sir[4]
                tip = sir[5]
                lista = modify(id, nr, suma, data, tip, lista, undoList, redoList)
            if sir[0] == "iesire":
                quit = True






