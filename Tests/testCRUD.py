from Domain.cheltuiala import getTip, getNr, getData, getSuma, getId, creeazaCheltuiala
from Logic.CRUD import adaugaCheltuiala, getByNr, stergeCheltuiala, modificaCheltuiala

def CheltuieliPentruTeste():
    '''
    creeaza mai multe cheltuieli
    :return:
    '''
    return [
        creeazaCheltuiala(1, 1, 100, "12.3.2000", "canal"),
        creeazaCheltuiala(2, 2, 300, "10.4.2012", "intretinere"),
        creeazaCheltuiala(3, 3, 450, "10.4.2018", "canal"),
        creeazaCheltuiala(4, 4, 600, "10.4.2016", "intretinere"),
        creeazaCheltuiala(5, 5, 250, "10.4.2020", "alte cheltuieli")
    ]


def testAdaugaCheltuiala():
    lista = []
    undoList = []
    redoList = []
    lista = adaugaCheltuiala(1, 1, 100, "12.3.2000", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 2, 300, "10.4.2012", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(3, 3, 450, "10.4.2018", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala(4, 4, 600, "10.4.2016", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(5, 5, 250, "10.4.2020", "alte cheltuieli", lista, undoList, redoList)

    assert len(lista) == 5
    assert getId(getByNr(1,lista)) == 1
    assert getNr(getByNr(1, lista)) == 1
    assert getSuma(getByNr(1, lista)) == 100
    assert getData(getByNr(1, lista)) == "12.3.2000"
    assert getTip(getByNr(1, lista)) == "canal"

    assert getId(getByNr(2, lista)) == 2
    assert getNr(getByNr(3, lista)) == 3
    assert getSuma(getByNr(4, lista)) == 600
    assert getData(getByNr(5, lista)) == "10.4.2020"
    assert getTip(getByNr(2, lista)) == "intretinere"

    # assert getNr(lista[0]) == 1
    # assert getSuma(lista[0]) == 200
    # assert getData(lista[0]) == "1.12.2000"
    # assert getTip(lista[0]) == "canal"


def testStergeCheltuiala():
    lista = CheltuieliPentruTeste()
    undoList = []
    redoList = []

    lista = stergeCheltuiala(1, lista, undoList, redoList)

    assert len(lista) == 4
    assert getByNr(1, lista) is None
    assert getByNr(2, lista) is not None

    lista = stergeCheltuiala(3, lista, undoList, redoList)
    assert len(lista) == 3
    assert getByNr(2, lista) is not None


def testModificaCheltuiala():
    lista = CheltuieliPentruTeste()
    undoList = []
    redoList = []

    lista = modificaCheltuiala(1, 1, 230, "13.04.2002", "intretinere", lista, undoList, redoList)
    cheltuialaNoua = getByNr(1, lista)
    assert getId(cheltuialaNoua) == 1
    assert getNr(cheltuialaNoua) == 1
    assert getSuma(cheltuialaNoua) == 230
    assert getData(cheltuialaNoua) == "13.04.2002"
    assert getTip(cheltuialaNoua) == "intretinere"

    cheltuialaNemodificata = getByNr(2, lista)
    assert getId(cheltuialaNemodificata) == 2
    assert getNr(cheltuialaNemodificata) == 2
    assert getSuma(cheltuialaNemodificata) == 300
    assert getData(cheltuialaNemodificata) == "10.4.2012"
    assert getTip(cheltuialaNemodificata) == "intretinere"





