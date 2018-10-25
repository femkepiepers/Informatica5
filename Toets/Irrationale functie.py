from math import sqrt as vierkantswortel
# invoer
a = float(input('Geef x: '))

# berekening + uitvoer
if a < 2:
    print('{:.2f} {} {}'.format(a, '∉ ', 'dom(f)'))
elif a == 2:
    print('{:.2f} {}'.format(a, 'is nulpunt van f'))
else:
    print('{}{:.2f}{} {} {:.2f}'.format('f(', a, ')', '=', vierkantswortel(a - 2)))