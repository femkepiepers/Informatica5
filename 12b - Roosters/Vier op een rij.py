def printbaar_rek(rek):
    i = len(rek) - 1
    a = 0
    mes = ''
    while i < len(rek):
        while rek[i][a] == 0:
            mes += 0
            a += 1
        while rek[i][a] == 'R':
            mes += 'R'
            a += 1
        while rek[i][a] == 'G':
            mes += 'G'
            a += 1
        i += -1
    return mes