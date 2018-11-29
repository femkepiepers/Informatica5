# invoer
aantal_basen = int(input('Aantal basen: '))
soorten_bases = 0
antw = ''

for i in range(aantal_basen):
    base = str(input('Base: '))
    for i in 'ATGC' or base not in antw:
        soorten_bases += 1
        if soorten_bases == 1:
            antw += base
            mes = 'De DNA-keting bevat 1 soort base: ' + antw
        elif soorten_bases == 2:
            antw += base
            mes = 'De DNA-keting bevat 2 verschillende soorten basen: ' + antw
        elif soorten_bases == 3:
            antw += base
            mes = 'De DNA-keting bevat 3 verschillende soorten basen: ' + antw
        elif soorten_bases == 4:
            antw += base
            mes = 'De DNA-keting bevat 4 verschillende soorten basen: ' + antw
print(mes)