def hoogtemeters(hoogtes):
    verschil = []
    i = 0
    while i < len(hoogtes) - 1:
        a = hoogtes[i + 1]
        b = a - hoogtes[i]
        verschil.append(b)
        i += 1

    return verschil

def dalen_en_stijgen(lijst):
    dalen = 0
    stijgen = 0

    for item in lijst:

        if item > 0:
            dalen += item

        elif item < 0:
            stijgen += item * -1

    return stijgen, dalen