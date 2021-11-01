

def creeazaCheltuiala(nr, suma, data, tip):
    '''
    creeaza o cheltuiala in care se specifica nr apartamentului, suma , data
    si tipul care poate sa fie (intretinere, canal, alte cheltuieli
    :param nr: int, numarul apartamentului
    :param suma: int, suma cheltuielii
    :param data: string, data in care se face cheltuiala
    :param tip: string, tipul cheltuielii
    :return: o cheltuiala cu datele introduse
    '''

    return{
        "nr": nr,
        "suma": suma,
        "data": data,
        "tip": tip
    }

def getNr(cheltuiala):
    '''
    da nr-ul apt unde ii cheltuiala
    :param cheltuiala:
    :return:
    '''

    return cheltuiala["nr"]


def getSuma(cheltuiala):
    '''
    da suma cheltuielii
    :param cheltuiala:
    :return:
    '''

    return cheltuiala["suma"]


def getData(cheltuiala):
    '''
    da data cheltuielii
    :param cheltuiala:
    :return:
    '''

    return cheltuiala["data"]


def getTip(cheltuiala):
    '''
    da tipul cheltuielii
    :param cheltuiala:
    :return:
    '''

    return cheltuiala["tip"]

def toString(cheltuiala):
    return "nr: {}, suma: {}, data: {}, tip: {}".format(
        getNr(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala),
    )