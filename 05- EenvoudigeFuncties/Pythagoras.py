# invoer
a = float(input('Geef lengte a: '))
b = float(input('Geef lengte b: '))
c = 'schuine zijde'
from math import sqrt as vierkantswortel

# berekening
linker_lid = vierkantswortel((a ** 2) + (b ** 2))
rechter_lid = c

#uitvoer
print('In een rechthoekige driehoek met rechthoekszijden ' + ' a = input(a) ' + ' en ' + ' b = input(b) ' + 'is de schuine zijde' + ' c')
