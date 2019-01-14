def positie_laagste_ascii(woord):
    mes = ''
    for i in range(0, len(woord)):
        a = ord(woord[i])
        if a > 32:
            mes = i
    return mes