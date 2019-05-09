def bestaat_weg(stad1, stad2, kaart):
    if stad1 in kaart[stad2]:
        mes = True
    else:
        mes = False
    return mes

def geen_dubbelburen(stad1, stad2, kaart):
    mes = {'Hasselt', 'Brussel', 'Antwerpen', 'Brugge', 'Gent', 'Kortrijk'}
    mes.remove(stad1)
    mes.remove(stad2)
    a = kaart[stad1].union(kaart[stad2])
    mes2 = a.difference(mes)
    return mes2

def bereikbaarheid_meest_afgelegen_stad(kaart):
    for i in range(len(kaart)):
        if len(kaart[i]) > 1:
            mes = len(kaart[i])
        else:
            mes = len(kaart[i])
    return mes

def bestaat_route(lijst, kaart):
    for i in range(len(kaart)):
        if bestaat_weg(lijst[i], lijst[i + 1], kaart) == True:
            mes = True
        else:
            mes = False
    return mes






kaart = {'Brugge': {'Gent', 'Antwerpen'}, 'Kortrijk': {'Gent'}, 'Gent': {'Antwerpen', 'Kortrijk', 'Brugge'}, 'Antwerpen': {'Gent', 'Brussel', 'Brugge'}, 'Brussel': {'Hasselt', 'Antwerpen'}, 'Hasselt': {'Brussel'}}
print(bestaat_route(['Brugge', 'Hasselt', 'Brussel'], kaart))