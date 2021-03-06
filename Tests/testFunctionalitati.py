from Logic.CRUD import adaugaCheltuiala, getByNr
from Logic.functionalitate import adunareCheltuieli, ordonare, CeaMaiMareCheltuialaPentruTip, sumeLunare
from Domain.cheltuiala import getSuma
from Tests.testCRUD import CheltuieliPentruTeste


def testAdaugaLaSuma():
    lista = []
    undoList = []
    redoList = []
    lista = adaugaCheltuiala(1, 1, 100, "12.3.2000", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 2, 300, "10.4.2012", "intretinere", lista, undoList, redoList)

    lista = adunareCheltuieli("12.3.2000", 100, lista)

    assert getSuma(getByNr(1, lista)) == 200

    # assert getSuma(lista[0]) == 200


def testCeaMaiMareCheltuialaPentruTip():
    lista = CheltuieliPentruTeste()

    rezultat = CeaMaiMareCheltuialaPentruTip(lista)

    assert len(rezultat) == 3
    assert getSuma(rezultat["alte cheltuieli"]) == 250
    assert getSuma(rezultat["canal"]) == 450
    assert getSuma(rezultat["intretinere"]) == 600



def testOrdonare():
    lista = CheltuieliPentruTeste()

    listaNoua = ordonare(lista)

    assert len(lista) == len(listaNoua)
    assert getSuma(listaNoua[0]) == 600
    assert getSuma(listaNoua[4]) == 100
    assert listaNoua[0] == lista[3]


def testSumeLunare():
    lista = CheltuieliPentruTeste()
    rezultatSume = sumeLunare(lista)
    rezultat = {}
    rezultat[3] = [100]
    rezultat[4] = [300, 450, 600, 250]
    assert len(rezultat) == len(rezultatSume)
    assert rezultat == rezultatSume










