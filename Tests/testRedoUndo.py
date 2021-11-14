from Domain.cheltuiala import getId
from Logic.CRUD import adaugaCheltuiala, getByNr, getById
from UI.console import doUndo, doRedo


def testUndoRedo():
    undoList = []
    redoList = []
    lista = []
    lista = adaugaCheltuiala(1, 1, 100, "12.3.2000", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 2, 300, "10.4.2012", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(3, 3, 450, "10.4.2018", "canal", lista, undoList, redoList)
    if len(undoList) > 0:
        lista = doUndo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getById(3,lista) is None
    assert len(lista) == 2

    if len(undoList) > 0:
        lista = doUndo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getByNr(2, lista) is None
    assert getByNr(3, lista) is None
    assert len(lista) == 1

    if len(undoList) > 0:
        lista = doUndo(lista, undoList, redoList)
    assert getByNr(1, lista) is None
    assert getByNr(2, lista) is None
    assert getByNr(3, lista) is None
    assert len(lista) == 0

    if len(undoList) > 0: #nu o sa faca nimic deoarece am dat undo deja la tot ce am adaugat
        lista = doUndo(lista, undoList, redoList)
    assert getByNr(1, lista) is None
    assert getByNr(2, lista) is None
    assert getByNr(3, lista) is None
    assert len(lista) == 0

    lista = adaugaCheltuiala(1, 1, 100, "12.3.2000", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala(2, 2, 300, "10.4.2012", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala(3, 3, 450, "10.4.2018", "canal", lista, undoList, redoList)
    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
        #nu se intampla nimic deoarece redo functioneaza doar dupa un undo
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getId(lista[2]) == 3
    assert len(lista) == 3

    if len(undoList) > 0:
        lista = doUndo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getById(3,lista) is None
    assert len(lista) == 2

    if len(undoList) > 0:
        lista = doUndo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getByNr(2, lista) is None
    assert getByNr(3, lista) is None
    assert len(lista) == 1

    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getById(3, lista) is None
    assert len(lista) == 2

    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getId(lista[2]) == 3
    assert len(lista) == 3

    if len(undoList) > 0:
        lista = doUndo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 2
    assert getById(3, lista) is None
    assert len(lista) == 2

    if len(undoList) > 0:
        lista = doUndo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getByNr(2, lista) is None
    assert getByNr(3, lista) is None
    assert len(lista) == 1

    lista = adaugaCheltuiala(4, 4, 600, "10.4.2016", "intretinere", lista, undoList, redoList)
    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
        #redo nu face nimic deoarece ultima actiune nu este un undo
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 4
    assert getByNr(2, lista) is None
    assert getByNr(3, lista) is None
    assert len(lista) == 2

    if len(undoList) > 0:
        lista = doUndo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getByNr(2, lista) is None
    assert getByNr(3, lista) is None
    assert len(lista) == 1

    if len(undoList) > 0:
        lista = doUndo(lista, undoList, redoList)
    assert getByNr(1, lista) is None
    assert getByNr(2, lista) is None
    assert getByNr(3, lista) is None
    assert len(lista) == 0

    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getByNr(2, lista) is None
    assert getByNr(3, lista) is None
    assert len(lista) == 1


    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 4
    assert getByNr(2, lista) is None
    assert getByNr(3, lista) is None
    assert len(lista) == 2

    if len(redoList) > 0:
        lista = doRedo(lista, undoList, redoList)
        #redo nu face nimic deoarece nu mai avem la ce sa dam undo
    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 4
    assert getByNr(2, lista) is None
    assert getByNr(3, lista) is None
    assert len(lista) == 2






