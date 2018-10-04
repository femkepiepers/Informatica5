x = float(input('x: '))
y = float(input('y: '))

linker_lid = abs(abs(x) - abs(y))
rechter_lid  = abs(x) - abs(y)



print('{:4f} ≤ {:4f}'.format(linker_lid, rechter_lid))