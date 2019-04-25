def beweeg(coördinaten, richting):

    if richting == '^':
        nieuwe_coördinaten = (coördinaten[0], coördinaten[1] + 1)

    elif richting == 'v':
        nieuwe_coördinaten = (coördinaten[0], coördinaten[1] - 1)

    elif richting == '>':
        nieuwe_coördinaten = (coördinaten[0] + 1, coördinaten[1])

    elif richting == '<':
        nieuwe_coördinaten = (coördinaten[0] - 1, coördinaten[1])

    return nieuwe_coördinaten

def teruggekeerd(richtingen):
    mes = False
    for i in range(0, len(richtingen) - 1):

        if richtingen[i] == '>' and richtingen[i + 1] == '<':
            mes = True

        elif richtingen[i] == '<' and richtingen[i + 1] == '>':
            mes = True

        elif richtingen[i] == 'v' and richtingen[i + 1] == '^':
            mes = True

        elif richtingen[i] == '^' and richtingen[i + 1] == 'v':
            mes = True

    return mes

def laatste_levende_positie(richtingen):
    geldige_zetten = 1
    start = [0, 0]
    i = 0
    nieuwe_coördinaten = beweeg(start, richtingen[i])

    while teruggekeerd(richtingen) is False and i in range(len(richtingen) - 1):

        nieuwe_coördinaten = beweeg(start, richtingen[i])
        geldige_zetten += 1
        i += 1

    return geldige_zetten, nieuwe_coördinaten[0], nieuwe_coördinaten[1]

print(laatst_levende_positie(['v', '>', 'v', '<', '^', '^']))