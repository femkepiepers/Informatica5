# invoer
a = float(input('Geef lengte a: '))
b = float(input('Geef lengte b: '))
c = 'schuine zijde'
from math import sqrt as vierkantswortel

# berekening
linker_lid = vierkantswortel((a ** 2) + (b ** 2))
rechter_lid = c

# uitvoer:
print('{} {} {:.2f} {} {} {:.2f} {} {:.2f}'.format('In een rechthoekige driehoek met rechthoekszijden', 'a =', a, 'en', 'b =', b, 'is de schuine zijde', linker_lid))