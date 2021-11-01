
from Domain.cheltuiala import creeazaCheltuiala, getTip, getSuma, getData, getNr, getId

def testCheltuiala():
    cheltuiala = creeazaCheltuiala(1, 1, 200, "1.12.2000", "canal")

    assert getId(cheltuiala) == 1
    assert getNr(cheltuiala) == 1
    assert getSuma(cheltuiala) == 200
    assert getData(cheltuiala) == "1.12.2000"
    assert getTip(cheltuiala) == "canal"

    # assert getNr(lista[0]) == 1
    # assert getSuma(lista[0]) == 200
    # assert getData(lista[0]) == "1.12.2000"
    # assert getTip(lista[0]) == "canal"