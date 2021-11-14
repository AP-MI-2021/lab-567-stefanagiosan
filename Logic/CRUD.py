from Domain.cheltuiala import creeazaCheltuiala, getNr, getId


def adaugaCheltuiala(id ,nr, suma, data, tip, lista , undoList, redoList):
    '''
    adauga o cheltuiala intr-o lista
    :param id: nr intreg
    :param nr: int
    :param suma: int
    :param data:  string
    :param tip: string
    :param lista: lista de cheltuieli
    :return: o lista continand atat elemente vechi cat si noua cheltuiala
    '''
    if getById(id, lista) is not None:
        raise ValueError("id-ul apartamentului exista deja!")
    if id < 0:
        raise ValueError("id-ul este negativ!")
    if nr < 0:
        raise ValueError("nr-ul este negativ!")
    if suma < 0:
        raise ValueError("suma este negativa!")
    if tip != "canal" and tip != "intretinere" and tip != "alte cheltuieli":
        raise ValueError("tipul cheltuielii nu se afla printre cele adaugate")
    cheltuiala = creeazaCheltuiala(id, nr, suma, data, tip)
    undoList.append(lista)
    redoList.clear()
    return lista + [cheltuiala]

def getByNr(nr, lista):
    '''
    da cheltuiala cu nr de apartament dat
    :param nr: int
    :param lista: lista de cheltuieli
    :return: cheltuiala cu nr-ul dat din lista sau none daca nu exista
    '''
    for cheltuiala in lista:
        if getNr(cheltuiala) == nr:
            return cheltuiala
    return None

def getById(id, lista):
    '''

    :param nr:
    :param lista:
    :return:
    '''
    for cheltuiala in lista:
        if getId(cheltuiala) == id:
            return cheltuiala
    return None


def stergeCheltuiala(nr, lista, undoList, redoList):
    '''

    :param nr: numarul apartamentului de la care vrem sa stergem cheltuiala
    :param lista: lista din care gasim numarul
    :return:
    '''
    if getByNr(nr, lista) is None:
        raise ValueError("Nu exista un apartament cu nr-ul dat!")
    if nr < 0:
        raise ValueError("nr-ul este negativ!")
    undoList.append(lista)
    redoList.clear()
    return [cheltuiala for cheltuiala in lista if getNr(cheltuiala) != nr]


def modificaCheltuiala(id ,nr, suma, data, tip, lista, undoList, redoList):
    '''
    modifica o prajitura dupa nr
    :param id: nr intreg
    :param nr: int
    :param suma: int
    :param data: string
    :param tip: string
    :param lista: lista pe care urmeaza sa o modificam
    :return: lista modificata
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista un apartament cu id-ul dat!")
    if id < 0:
        raise ValueError("id-ul este negativ!")
    if nr < 0:
        raise ValueError("nr-ul este negativ!")
    if suma < 0:
        raise ValueError("suma este negativa!")
    if tip != "canal" and tip != "intretinere" and tip != "alte cheltuieli":
        raise ValueError("tipul cheltuielii nu se afla printre cele adaugate")
    listaNoua = []
    for cheltuiala in lista:
        if getNr(cheltuiala) == nr:
            cheltuialaNoua = creeazaCheltuiala(id ,nr, suma, data, tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    undoList.append(lista)
    redoList.clear()
    return listaNoua

