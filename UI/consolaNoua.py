from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala


def help():
    print("Pentru crearea unei cheltuieli trebuie citite id-ul (nr intreg) , numarul apt. (nr intreg) , suma (nr intreg) , data si tipul cheltuielii ")
    print("Cheltuielile se adauga in lista cu functia 'add' si trebuie sa se introduca valori adecvate ")
    print("Toate cheltuielile din lista se afiseaza cu functia 'showall' ")
    print("cheltuielile se pot sterge scriind 'delete' introducandu-se nr-ul cheltuielii, aceasta trebuie sa existe")
    print("Comenzile trebuie apelate pe o linie ,separate prin ' ; ' iar campurile prin ' , '  ")
    print("Sa nu se foloseasca alti separatori!")
    print("pentru a iesi din meniu scrieti la comenzi 'iesire'")





def add(id, nr, suma, data, tip, lista):

    try:
        lista = adaugaCheltuiala(id, nr, suma, data, tip, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
    print("cheltuiala a fost adaugata")
    return lista

def delete(nr, lista):
    try:
        lista = stergeCheltuiala(nr, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
    print("stergerea a fost facuta")
    return lista

def showall(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))

def mofify(id, nr, suma, data, tip, lista):
    try:
        lista = modificaCheltuiala(id, nr, suma, data, tip, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
    print("modificarea a fost facuta")
    return lista


def runNewMenu(lista):
    quit = False
    while not quit:
        help()
        optiune = input("dati comenzile: ")
        optiuni = optiune.split(';')
        for comenzi in optiuni:
            sir = comenzi.split(',')
            if sir[0] == "add":
                id = sir[1]
                nr = sir[2]
                suma = sir[3]
                data = sir[4]
                tip = sir[5]
                lista = add(id, nr, suma, data, tip, lista)
            if sir[0] == "delete":
                nr = sir[1]
                lista = delete(nr, lista)
            if sir[0] == "showall":
                showall(lista)
            if sir[0] == "iesire":
                quit = True
            else:
                print("optiune gresita! reincarcati")





