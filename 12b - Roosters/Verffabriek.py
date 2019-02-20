def kleur_toevoegen(verwerkt, kleur):

    if kleur == 'rood':
        verwerkt[0] += 1
    elif kleur == 'groen':
        verwerkt[1] += 1
    elif kleur == 'blauw':
        verwerkt[2] += 1

    return verwerkt

def is_wit(verwerkt):

    if verwerkt[0] == verwerkt[1] == verwerkt[2]:
        mes = True
    else:
        mes = False

    return mes

def verf_verzamelen(kleuren):
    start = [0, 0, 0]
    start = kleur_toevoegen(start, kleuren[0])
    i = 1
    while is_wit(start) is False and i in range(len(kleuren)):
        start = kleur_toevoegen(start, kleuren[i])
        i += 1

    if is_wit(start) is True:
        mes = i, start

    elif is_wit(start) is False:
        mes = None

    return mes
