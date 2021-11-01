from Domain.cheltuiala import getNr, getSuma, getData, getTip, creeazaCheltuiala

def adunareCheltuieli(data, valoarea, lista):
    '''
    aduna la cheltuieli o valoarea pentru cheltuielile dintr-o data citita
    :param data: string
    :param valoarea: float
    :param lista: lista de prajituri
    :return:
    '''
    listaNoua = []
    for cheltuiala in lista:
        if data == getData(cheltuiala):
            cheltuialaNoua = creeazaCheltuiala(
                getNr(cheltuiala),
                getSuma(cheltuiala) + valoarea,
                getData(cheltuiala),
                getTip(cheltuiala),
            )
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua
