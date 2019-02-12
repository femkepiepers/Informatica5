def nieuw_kaartspel(kleuren, waardes):
    mes = []
    i = 0
    a = 0

    while i in range(len(kleuren)):

        while a != len(waardes):
            mes.append(kleuren[i] + waardes[a])
            a += 1
        i += 1
        a = 0
    return mes

def splits_kaartspel(lijst):
    a = len(lijst)
    b = len(lijst) // 2
    splits_1 = lijst[:b]
    splits_2 = lijst[b:]

    return splits_1, splits_2

def faro_shuffle(splits_1, splits_2):
    faro_lijst = []
    i = 0
    a = 0
    while i in range(len(splits_1)) and a in range(len(splits_2)):
        faro_lijst.append(splits_1[i])
        faro_lijst.append(splits_2[a])
        a += 1
        i += 1

    if len(splits_1) < len(splits_2):
        faro_lijst.append(splits_2[a])

    return faro_lijst