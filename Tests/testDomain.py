
from Domain.cheltuiala import creeazaCheltuiala, getTip, getSuma, getData, getNr

def testCheltuiala():
    cheltuiala = creeazaCheltuiala(1, 200, "1.12.2000", "canal")

    assert getNr(cheltuiala) == 1
    assert getSuma(cheltuiala) == 200
    assert getData(cheltuiala) == "1.12.2000"
    assert getTip(cheltuiala) == "canal"