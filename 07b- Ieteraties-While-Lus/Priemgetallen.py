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

/////////////////////////////////////////////////////////////////////////////////////////////////

getal = int(input('Getal: '))

# zolang je het niet kan delen door 2, 3, 4 is het allicht geen priemgetal

deler = 2

while getal % deler != 0 and getal != 1:
    deler += 1
    print(deler)
if deler == getal:
    print('priemgetal')
else:
    print('geen priemgetal')