def vergeten_woorden(tekst, verplicht):
    verzameling = set(tekst.split())
    verplichte_woorden = len(verplicht)
    vergeten_woorden = len(verplicht.difference(verzameling))
    gebruikte_woorden = verplichte_woorden - vergeten_woorden

    return verplichte_woorden, vergeten_woorden, gebruikte_woorden