def geldige_zet(zet):

    mes = False
    if len(zet) == 3 and zet[0] in 'KDTLP'and zet[1] in 'abcdefgh' and zet[2] in '12345678':
        mes = True

    elif len(zet) == 2 and zet[0] in 'abcdefgh' and zet[1] in '123456784':
        mes = True

    return mes

def geldige_zetten(zetten):
    mes = True
    a = 0
    b = len(zetten)
    while mes == True and a in range(0, b - 1):

        mes = geldige_zet(zetten[a])
        a += 1

    return mes

#  VERBETERING KLAS
def geldige_zetten(zetten):

    i = 0
    while i < len(zetten) and geldige_zetten([i]):
        i += 1
    return i >= len(zetten)