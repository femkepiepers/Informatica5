def nieuw_kaartspel(kleuren, waardes):
    mes = []
    i = 0
    a = 0

    while i in range(len(kleuren)):

        while a != len(waardes):
            mes.append(kleuren[i] + waardes[a])
            a += 1
        i += 1
    return mes