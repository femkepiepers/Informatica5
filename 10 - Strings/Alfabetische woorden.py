def positie_laagste_ascii(woord):
    a = 10000
    for i in range(0, len(woord)):
        if ord(woord[i]) < a:
            a = ord(woord[i])
    b = chr(a)
    mes = woord.find(b)
    return mes

def sorteer(woord):
    nieuwe_woord = ''
    for i in range(0, len(woord)):
        a = 10000
        for i in range(0, len(woord)):
            if ord(woord[i]) < a:
                a = ord(woord[i])
        b = chr(a)
        nieuwe_woord += b
        z = woord.find(b)
        woord = woord[0:z] + woord[z + 1:]
    return nieuwe_woord

def is_alfabetisch(woord):
    b = sorteer(woord)
    if b == woord:
        mes = True
    else:
        mes = False
    return mes