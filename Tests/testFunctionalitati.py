from Logic.CRUD import adaugaCheltuiala, getByNr
from Logic.functionalitate import adunareCheltuieli
from Domain.cheltuiala import getSuma

def testAdaugaLaSuma():
    lista = []
    lista = adaugaCheltuiala(1, 1, 100, "12.3.2000", "canal", lista)
    lista = adaugaCheltuiala(2, 2, 300, "10.4.2012", "intretinere", lista)

    lista = adunareCheltuieli("12.3.2000", 100, lista)

    assert getSuma(getByNr(1, lista)) == 200

    # assert getSuma(lista[0]) == 200