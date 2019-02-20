def volgende_rij(rij):
    next = []
    for i in range(0, len(rij) - 1):

        if rij[i] == rij[i + 1]:
            next.append(rij[i])

        elif rij[i] != rij[i + 1]:
            kleur = ['Y', 'R', 'G']
            kleur.remove(rij[i])
            kleur.remove(rij[i + 1])
            next.append(kleur[0])

    return next

def driehoek(rij):
    helemaal = []
    i = 0
    helemaal.append(rij)

    while len(helemaal[i]) > 1:
        next = volgende_rij(helemaal[i])
        helemaal.append(next)
        i += 1

    return helemaal

def kleuren(driehoek):
    geel = 0
    rood = 0
    groen = 0

    for i in range(len(driehoek)):

        for a in range(len(driehoek[i])):

            kleur = driehoek[i][a]
            if kleur == 'G':
                groen += 1

            elif kleur == 'R':
                rood += 1

            elif kleur == 'Y':
                geel += 1

    return groen, rood, geel

