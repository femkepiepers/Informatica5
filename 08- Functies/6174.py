def splits(a):
    getal_1 = a / 1000
    getal_2 = (a - (getal_1 * 1000)) / 100
    getal_3 = (a - (getal_1 * 1000) - (getal_2 * 100)) / 10
    getal_4 = a - (getal_1 * 1000) - (getal_2 * 100) - (getal_3 * 10)
    return getal_1, getal_2, getal_3, getal_4

def oplopende_cijfers(b, c, d, e):
    getal_1 = min(b, c, d, e)
    getal_2 = max(min(b, c, d), min(b, c, e), min(b, d, e), min(c, d, e))
    getal_3 = min(max(b, c, d), max(b, c, e), max(b, d, e), max(c, d, e))
    getal_4 = max(b, c, d, e)
    return getal_1, getal_2, getal_3, getal_4

def op_af_getallen(f, g, h, i):
    op_getallen = ''
    af_getallen = ''
    op_getallen += str(f) + str(g) + str(h) + str(i)
    af_getallen += str(i) + str(h) + str(g) + str(f)
    return op_getallen, af_getallen

def verschil(j, k):
    verschil = str(int(j) - int(k))
    return verschil

def kaprekar(l):