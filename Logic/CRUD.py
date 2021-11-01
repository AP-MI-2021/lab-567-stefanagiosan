from Domain.cheltuiala import creeazaCheltuiala, getNr

def adaugaCheltuiala(nr, suma, data, tip, lista ):
    '''
    adauga o cheltuiala intr-o lista
    :param nr: int
    :param suma: int
    :param data:  string
    :param tip: string
    :param lista: lista de cheltuieli
    :return: o lista continand atat elemente vechi cat si noua cheltuiala
    '''
    cheltuiala = creeazaCheltuiala(nr, suma, data, tip)
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


def stergeCheltuiala(nr, lista):
    '''

    :param nr:
    :param lista:
    :return:
    '''
    return [cheltuiala for cheltuiala in lista if getNr(cheltuiala) != nr]


def modificaCheltuiala(nr, suma, data, tip, lista):
    '''
    modifica o prajitura dupa nr
    :param nr:
    :param suma:
    :param data:
    :param tip:
    :param lista:
    :return:
    '''
    listaNoua = []
    for cheltuiala in lista:
        if getNr(cheltuiala) == nr:
            cheltuialaNoua = creeazaCheltuiala(nr, suma, data, tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua