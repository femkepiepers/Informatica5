# invoer
kaart = int(input('kaart: '))
som = 0

# berekining
while som < 21 and kaart > 0:
    som += kaart
    if som < 21:
        kaart = int(input('kaart: '))

if kaart == 0:
    mes = 'Voorzichtig gespeeld ({})'.format(som)

if som == 21:
    mes = 'Gewonnen!'

if som > 21:
    mes = 'Verbrand ({})'.format(som)

# uitvoer
print(mes)


