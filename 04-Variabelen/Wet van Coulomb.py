k = 8.99*10**9
Q1 = 2.0 * 10**-6
Q2 = 1.0 * 10**-6

# invoer
r = float(input('Geef straal: '))

# berekening
fc = k * ((Q1 * Q2)/(r * 10**-2)** 2)

# uitvoer
resultaat = 'De coulombkracht = '

print(fc)