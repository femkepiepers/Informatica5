def hint(gok, woord):
    antw = '.....'
    if gok[0] == woord[0]:
        antw = antw.replace([0], [0].upper())
    elif gok[1] == woord[1]:
        antw = antw.replace([1], [1].upper())
    elif gok[2] == woord[2]:
        antw = antw.replace([2], [2].upper())
    elif gok[3] == woord[3]:
        antw = antw.replace([3], [3].upper())
    elif gok[4] == woord[4]:
        antw = antw.replace([4], [4].upper())
    elif gok[:] in woord[:]:
        antw : antw.replace()






    return antw