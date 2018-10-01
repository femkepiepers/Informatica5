# gegeven
x= 'bedrag in eurocenten'

# invoer
x = int(input('Geef bedrag in eurocenten: '))

# berekening
aantal_muntjes = x // 100
r = x % 100

aantal_muntjes += (r // 50)
r %= 50

aantal_muntjes += (r // 20)
r = r % 20

aantal_muntjes += (r // 10)
r = r % 10

aantal_muntjes += (r // 5)
r = r  % 5

aantal_muntjes += (r // 2)
r = r % 2

aantal_muntjes += (r // 1)
r = r % 1

aantal_muntjes += r

# uitvoer
print(str(x) + ' cent kan je omwisselen in ' + str(aantal_muntjes) + ' muntstukken ')
