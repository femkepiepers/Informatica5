# Middagmaal: € 5.3
# Soep: € 1.7
# Vieruurtje: € 2.3
def maaltijdprijs(type, aantal):
    maaltijdprijs = 0

    if type == 'middagmaal':
        maaltijdprijs = aantal * 5.3
    elif type == 'soep':
        maaltijdprijs = aantal * 1.7
    elif type == 'vieruurtje':
        maaltijdprijs = aantal * 2.3

    return maaltijdprijs

def dagprijs(bestelling):

    dagprijs = 0
    # overloop alle bestellingen in stapjes van 2
    for i in range(0, len(bestelling), 2):

        dagprijs += maaltijdprijs(bestelling[i], bestelling[i + 1])

    return dagprijs

def weekprijs(bestellingen):

    weekprijs = 0
    for dag in bestellingen:

        weekprijs += dagprijs(dag)

    return weekprijs