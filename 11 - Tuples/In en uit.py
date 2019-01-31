from math import sqrt
def binnen_of_buiten(m, c, p):
    # straal berekenen: d(m, c) + kan je ook met pow doen!!
    r = sqrt(pow(m[0] - c[0], 2) + pow(m[1] - c[1], 2))
    #r = sqrt(((m[0] - c[0]) ** 2) + ((m[1] - c[1]) ** 2))

    # afstand_mp berekenen: d(m, p)
    d = sqrt(((m[0] - p[0]) ** 2) + ((m[1] - p[1]) ** 2))

    if r == d:
        mes = 'op'
    elif r > d:
        mes = 'binnen'
    else:
        mes = 'buiten'

    return mes, round(d,4)

print(binnen_of_buiten((0, 0),(1, 1),(-1, -1)))