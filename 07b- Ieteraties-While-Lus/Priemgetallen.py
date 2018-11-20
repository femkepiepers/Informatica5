# invoer
getal = int(input('Getal: '))
a = 2
b = 1

# berekening
while a < getal:
    if (getal % a) == 0:
        mes = '{} is geen priemgetal'.format(getal)
        b = 0
    a += 1
if b and getal != 1:
    mes = '{} is een priemgetal'.format(getal)
elif getal == 1:
    mes = '1 is geen priemgetal'

# uitvoer
print(mes)