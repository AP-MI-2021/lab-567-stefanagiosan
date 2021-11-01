

def creeazaCheltuiala(id ,nr, suma, data, tip):
    '''
    creeaza o cheltuiala in care se specifica nr apartamentului, suma , data
    si tipul care poate sa fie (intretinere, canal, alte cheltuieli
    :param id: o valoare intreaga
    :param nr: int, numarul apartamentului
    :param suma: int, suma cheltuielii
    :param data: string, data in care se face cheltuiala
    :param tip: string, tipul cheltuielii
    :return: o cheltuiala cu datele introduse
    '''
    # return [id,nr, suma, data, tip]
    return{
        "id": id,
        "nr": nr,
        "suma": suma,
        "data": data,
        "tip": tip
    }

def getId(cheltuiala):
    '''
    id-ul unei cheltuieli
    :param cheltuiala:
    :return: o valoare intreaga
    '''
    return cheltuiala["id"]


def getNr(cheltuiala):
    '''
    da nr-ul apt unde ii cheltuiala
    :param cheltuiala:
    :return:
    '''
    #return cheltuiala[0]
    return cheltuiala["nr"]


def getSuma(cheltuiala):
    '''
    da suma cheltuielii
    :param cheltuiala:
    :return:
    '''
    #return cheltuiala[1]
    return cheltuiala["suma"]


def getData(cheltuiala):
    '''
    da data cheltuielii
    :param cheltuiala:
    :return:
    '''
    # return cheltuiala[2]
    return cheltuiala["data"]


def getTip(cheltuiala):
    '''
    da tipul cheltuielii
    :param cheltuiala:
    :return:
    '''
    #return cheltuiala[3]
    return cheltuiala["tip"]

def toString(cheltuiala):
    return "id: {} ,nr: {}, suma: {}, data: {}, tip: {}".format(
        getId(cheltuiala),
        getNr(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala),
    )