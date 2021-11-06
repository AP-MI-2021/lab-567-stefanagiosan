
 #from Domain.cheltuiala import getData
 '''

def sumeLunare(lista):


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
    '''
