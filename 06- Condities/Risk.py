# invoer
a = float(input('Aantal ogen dobbelsteen 1 aanvaller: '))
b = float(input('Aantal ogen dobbelsteen 2 aanvaller: '))
c = float(input('Aantal ogen dobbelsteen 3 aanvaller: '))
d = float(input('Aantal ogen dobbelsteen 1 verdediger: '))
e = float(input('Aantal ogen dobbelsteen 2 verdediger: '))

# berekening
f = max(a, b, c)
h = min(a, b, c)
i = max(d, e)
j = a + b + c - f - h
k = d + e - i

# uitvoer
if f > i and j > k:
    print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
if f <= i and j <= k:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
if f <= i and j > k or f > i and j <= k:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')