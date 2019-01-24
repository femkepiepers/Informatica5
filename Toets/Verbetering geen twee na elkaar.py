def ontdubbelen(woord):
    nieuwe_woord = woord[0]

    for i in range(1, len(woord)):

        if woord[i] != woord[i -1]:
            nieuwe_woord += woord[i]

    return nieuwe_woord