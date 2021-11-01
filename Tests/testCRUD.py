from Domain.cheltuiala import getTip, getNr, getData, getSuma
from Logic.CRUD import adaugaCheltuiala, getByNr, stergeCheltuiala

def testAdaugaCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, 100, "12.3.2000", "canal", lista )

    assert len(lista) == 1
    assert getNr(getByNr(1, lista)) == 1
    assert getSuma(getByNr(100, lista)) == 100
    assert getData(getByNr("12.3.2000", lista)) == "12.3.2000"
    assert getTip(getByNr("canal", lista)) == "canal"


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