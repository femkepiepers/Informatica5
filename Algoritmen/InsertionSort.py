from time import time
from random import randint
import matplotlib.pyplot as plt

def genereer_rij(aantal):
    rij = []
    for i in range(aantal):
        rij.append(randint(0, aantal))
    return rij

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

    return a


i, n, t_insertion, t_python = 10, [], [], []

while i < 2000:

    rij_1 = genereer_rij(i)
    rij_2 = rij_1.copy()

    # insertion sort testen
    start = time()
    insertion_sort(rij_1)
    stop = time()
    t_insertion.append(stop - start)

    # sorteerfunctie van python testen
    start = time()
    rij_2.sort()
    stop = time()
    t_python.append(stop - start)

    n.append(i)
    i += 50

plt.plot(n, t_insertion, '-b')
plt.plot(n, t_python, '-r')
plt.title('insertion sort')
plt.gca().legend(('insertion sort', 'python sort'))
plt.xlabel('N')
plt.ylabel('t')
plt.gcf().canvas.set_window_title('Femke Piepers')
plt.show()