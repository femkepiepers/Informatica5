def geldige_zet(zet):

    if zet[0] in 'KDTLP'and zet[1] in 'abcdefgh' and zet[2] in '12345678':
        mes = True

    elif zet[0] in 'abcdefgh' and zet[1] in '123456784':
        mes = True

    else:
        mes = False

    return mes

def geldige_zetten(zetten):
    mes = True
    a = 0
    b = len(zetten)
    while mes == True and a in range(0, b - 1):

        mes = geldige_zet(zetten[a])
        a += 1

    return mes