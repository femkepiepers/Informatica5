def woord_frequentie(tekst):

    mes = {}
    tekst = tekst.lower()
    tekst = tekst.replace('.', ' ')
    tekst = tekst.split()
    for item in tekst:

        if item not in mes:
            totaal = tekst.count(item)
            mes[item] = totaal

    return mes

def woorden_per_frequentie(tekst):

    mes = {}
    totaal = woord_frequentie(tekst)
    for key, value in totaal.items():

        if value not in mes:
            mes[value] = [key]

        else:
            mes[value].append(key)

    return mes

def meest_gebruikte_woorden(tekst):

    aantal = woorden_per_frequentie(tekst)
    hoogste = max(aantal.keys())
    mes = aantal.get(hoogste)

    return mes
