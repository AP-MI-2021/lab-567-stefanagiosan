from Domain.cheltuiala import getTip, getNr, getData, getSuma
from Logic.CRUD import adaugaCheltuiala, getByNr, stergeCheltuiala, modificaCheltuiala

def testAdaugaCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, 100, "12.3.2000", "canal", lista )

    assert len(lista) == 1
    assert getNr(getByNr(1, lista)) == 1
    assert getSuma(getByNr(1, lista)) == 100
    assert getData(getByNr(1, lista)) == "12.3.2000"
    assert getTip(getByNr(1, lista)) == "canal"


def testStergeCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, 100, "12.3.2000", "canal", lista)
    lista = adaugaCheltuiala(2, 300, "10.4.2012", "intretinere", lista)

    lista = stergeCheltuiala(1, lista)

    assert len(lista) == 1
    assert getByNr(1, lista) is None
    assert getByNr(2, lista) is not None

    lista = stergeCheltuiala(3, lista)
    assert len(lista) == 1
    assert getByNr(2, lista) is not None


def testModificaCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, 100, "12.3.2000", "canal", lista)
    lista = adaugaCheltuiala(2, 300, "10.4.2012", "intretinere", lista)

    lista = modificaCheltuiala(1, 230, "13.04.2002", "intretinere", lista)
    cheltuialaNoua = getByNr(1, lista)
    assert getNr(cheltuialaNoua) == 1
    assert getSuma(cheltuialaNoua) == 230
    assert getData(cheltuialaNoua) == "13.04.2002"
    assert getTip(cheltuialaNoua) == "intretinere"

    cheltuialaNemodificata = getByNr(2, lista)
    assert getNr(cheltuialaNemodificata) == 2
    assert getSuma(cheltuialaNemodificata) == 300
    assert getData(cheltuialaNemodificata) == "10.4.2012"
    assert getTip(cheltuialaNemodificata) == "intretinere"


