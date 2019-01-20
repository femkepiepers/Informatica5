def doe_maar_gewoon(woord):
    for i in range(0, len(woord) + 1):
        if woord[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if woord[i + 1] == woord[i].lower():
                woord = woord[0:i - 1] + woord[i].lower() + woord[i:]
    return woord