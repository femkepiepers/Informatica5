pi = 3.14159

# invoer
r = float(input('Geef straal: '))

# berekening
opp_cirkel = pi *(r ** 2)

# De oppervlakte van een cirkel met straal 2.0 is 12.56636

# uitvoer
resultaat = 'De oppervlakte van een cirkel met straal '
resultaat += str(r) + ' is ' + str(opp_cirkel)

print(resultaat)