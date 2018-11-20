# invoer
totaal = 0
prijs = 1

# berekening
while prijs > 0:
    prijs = float(input('prijs : '))
    totaal += prijs

# uitvoer
print('De totale prijs is €', '{:.2f}'.format(totaal))