def volgende_rij(rij):
    lijst = []
    i = 0
    for i in range(0, len(lijst)):
        if rij[i] == rij[i + 1]:
            lijst.append('rij[i]')
        elif rij[i] != rij[i + 1]:
            lijst.append('rij')