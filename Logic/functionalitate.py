from Domain.cheltuiala import getNr, getSuma, getData, getTip, creeazaCheltuiala, getId

def adunareCheltuieli(data, valoarea, lista):
    '''
    aduna la cheltuieli o valoarea pentru cheltuielile dintr-o data citita
    :param data: string
    :param valoarea: int
    :param lista: lista de prajituri
    :return:
    '''
    listaNoua = []
    for cheltuiala in lista:
        if data == getData(cheltuiala):
            cheltuialaNoua = creeazaCheltuiala(
                getId(cheltuiala),
                getNr(cheltuiala),
                getSuma(cheltuiala) + valoarea,
                getData(cheltuiala),
                getTip(cheltuiala),
            )
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua


def CeaMaiMareCheltuialaPentruTip(lista):
    '''
    functia returneaza cheltuiala care are cea mai mare suma pentru fiecare tip de cheltuiala

    :param lista: o lista de cheltuieli
    :return: un dictionar, unde cheia este "tipul cheltuielii" ,iar valoarea este cheltuiala
    '''


    rezultat = {}
    for cheltuiala in lista:
        tip = getTip(cheltuiala)
        suma = getSuma(cheltuiala)
        if tip not in rezultat:
            rezultat[tip] = cheltuiala
        else:
            if suma > getSuma(rezultat[tip]):
                rezultat[tip] = cheltuiala
    return rezultat



def ordonare(lista):
    '''
    functia ordoneaza descrescator dupa suma
    :param lista: lista de cheltuieli
    :return: lista ordonata descrescator , key = fiind dupa cheltuielilor
    '''

    return sorted(lista, key = getSuma , reverse = True)

def sumeLunare(lista):
    '''

    :param lista:  lista de cheltuieli
    :return:
    '''

    rezultat = {}
    for cheltuiala in lista:
        data = getData(cheltuiala)
        luna = int(data.split('.')[1])
        if luna not in rezultat:
            rezultat[luna] = []
            rezultat[luna].append(getSuma(cheltuiala))
        else:
            rezultat[luna].append(getSuma(cheltuiala))
    return rezultat
