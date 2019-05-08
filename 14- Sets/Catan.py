def wisselen_mogelijk(ruilmarkt, wens, verzameld):
    ruilmarkt = {'goud': {'erts', 'wol', 'steen'}, 'wol': {'erts', 'steen', 'hout'}, 'erts': {'hout', 'steen'}, 'steen': {'hout', 'graan'}}

    mes = set(verzameld)

    return mes.issubset(ruilmarkt[wens])