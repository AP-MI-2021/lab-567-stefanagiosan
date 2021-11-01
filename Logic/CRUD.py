from Domain.cheltuiala import creeazaCheltuiala, getNr

def adaugaCheltuiala(id ,nr, suma, data, tip, lista ):
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
    cheltuiala = creeazaCheltuiala(id, nr, suma, data, tip)
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


def modificaCheltuiala(id ,nr, suma, data, tip, lista):
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
    listaNoua = []
    for cheltuiala in lista:
        if getNr(cheltuiala) == nr:
            cheltuialaNoua = creeazaCheltuiala(id ,nr, suma, data, tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua