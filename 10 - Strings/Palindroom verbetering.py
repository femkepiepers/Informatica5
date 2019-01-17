#len(woord) dan controleer je het hele woord!!!!
# controleren tot je een verschil tegenkomt!!
def palindroom(woord):

    i = 0

    while woord[i] == woord[-i - 1] and i < len(woord) // 2:
        i += 1
    return i == (len(woord) // 2)


print(palindroom(1000 * 'a'))


#OF
return woord == woord[::1] 