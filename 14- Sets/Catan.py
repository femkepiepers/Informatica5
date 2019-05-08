def wisselen_mogelijk(ruilmarkt, wens, verzameld):
    if ruilmarkt[wens].issubset(verzameld):
        mes = True
    else:
        mes = False
    return mes

def bereken_ruilmiddelen(ruilmarkt, wensen, verzameld):
    if