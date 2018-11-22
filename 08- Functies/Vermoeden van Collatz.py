def volgend_collatz_getal(n):
    if n % 2 == 0:
        volgend = n // 2
    else:
        volgend = (n * 3) + 1
    return volgend

print(volgend_collatz_getal(88))

def cyclelengte