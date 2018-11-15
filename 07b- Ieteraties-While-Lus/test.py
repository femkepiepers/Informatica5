from random import randint
temp = randint(-10, 5)
vorst_periode = 0

while temp < 0:
    print(temp)
    vorst_periode += 1
    temp = randint(-10, 5)

print(vorst_periode, 'dagen')