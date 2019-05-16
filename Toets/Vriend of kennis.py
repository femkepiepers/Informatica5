def vriend_of_kennis(kennissen, persoon_a, persoon_b):
    if persoon_a in kennissen[persoon_b] and persoon_b not in kennissen[persoon_a]:
        mes = {}.format(persoon_a, 'kent', persoon_b)
    elif persoon_b in kennissen[persoon_a] and persoon_a not in kennissen[persoon_b]:
        mes = 'persoon_a kent persoon_b'
    elif persoon_a in kennissen[persoon_b] and persoon_b in kennissen[persoon_a]:
        mes = 'persoon_a en persoon_b zijn vrienden'
    elif persoon_a not in kennissen[persoon_b] and persoon_b not in kennissen[persoon_a]:
        mes = 'persoon_a en persoon_b kennen elkaar niet'

    return mes
kennissen = {'Eva': {'Margaux', 'Arno'}, 'Arno': {'Eva', 'Jens'}, 'Jens': {'Margaux', 'Eva'}, 'Margaux': set()}
print(vriend_of_kennis(kennissen, 'Arno', 'Eva'))

# def unieke_kennissen