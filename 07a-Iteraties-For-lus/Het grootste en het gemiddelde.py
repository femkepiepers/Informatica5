# invoer
aantal_getallen = int(input('aantal getallen: '))
getal = ''
som = ''

for i in range(aantal_getallen):
    getal = input('Getal: ')

# Berekening
max = max(getal)
som += getal
#gemiddelde = ((int(som)) / (int(aantal_getallen)))

#uitvoer
print(max, som)
