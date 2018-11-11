# invoer
aantal_getallen = int(input('aantal getallen: '))
max = 0
som = 0

for i in range(aantal_getallen):
    getal = int(input('Getal: '))
    if i == 0:
        max = getal
    elif getal > max:
        max = getal
    som += getal

# Berekening gemiddelde
gemiddelde = round((som / aantal_getallen), 2)



#uitvoer
print(max, gemiddelde)
