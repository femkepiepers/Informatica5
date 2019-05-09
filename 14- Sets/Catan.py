def wisselen_mogelijk(ruilmarkt, wens, verzameld):
    if ruilmarkt[wens].issubset(verzameld):
        mes = True
    else:
        mes = False
    return mes

def bereken_ruilmiddelen(ruilmarkt, wens):
    mes = {}
    for i in range(len(wens)):
        lijst = list(ruilmarkt[wens[i]])
        for b in range(len(lijst)):
            if lijst[b] in mes:
                mes[lijst[b]] += 1
            else:
                mes[lijst[b]] = 1
    return mes