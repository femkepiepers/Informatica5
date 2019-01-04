# input
getal = int(input('Getal: '))
volgend_getal = ''
cyclelengte = 0

# volgend getal berekenen
if getal % 2 == 0:
    volgend_getal = getal // 2
elif getal % 2 != 0:
    volgend_getal = (getal * 3) + 1

# cyclelengte berekenen
while volgend_getal != 1:
    if getal % 2 == 0:
        volgend_getal = getal // 2

    elif getal % 2 != 0:
        volgend_getal = (getal * 3) + 1
    cyclelengte += 1

# uitvoer
print(volgend_getal)
print(cyclelengte)