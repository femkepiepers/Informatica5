# invoer
dv = float(input('Geef dv: '))
vv = float(input('Geef vv: '))
da = float(input('Geef da: '))
va = float(input('Geef va: '))

# berekening
pv = min(((vv * dv) / 40), 1)
pa = min(((va * da) / 40), 1)

# code bepalen
if min(pv, pa) > 0.7:
    mes = 'zwart'
elif max(pv, pa) > 0.7 and abs(pv - pa) < 0.2:
    mes = 'rood'
elif abs(pv - pa) > 0.7:
    mes = 'geel'
else:
    mes = 'groen'

# uitvoer
print(mes)