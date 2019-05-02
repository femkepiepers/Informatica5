def behoort_tot_taal(woord, taal):

    mes = set(woord)
    mes.discard(' ')

    return mes.issubset(taal) and len(mes) > 0

def is_onleesbaar(woord, taal):
    mes = set(woord)
    mes.discard(' ')

    return mes.isdisjoint(taal)

def perfect_woord(woord, taal):
    mes = set(woord)
    mes.discard(' ')

    return taal.issubset(mes)