# invoer
#woord = str(input('Geef woord: '))
#nieuwe_woord = ''

# berekeningen
#for i in range(0, len(woord) + 1):
   # if woord[i] == woord[i + 1]:
           # nieuwe_woord += woord[0:i] + woord[i + 2:]
   # elif woord[i + 1] == woord[i + 2]:
            #nieuwe_woord += woord[0:i] + woord[i + 3:]

# uitvoer
#print(nieuwe_woord)

def ontdubbelen(woord):
    nieuwe_woord = ''

    for i in range(0, len(woord) + 1):

        if woord[i] == woord[i + 1:].find('woord[i]'):
            nieuwe_woord += woord[0:i] + woord[a + 1:]

    return nieuwe_woord

print(ontdubbelen('aaien'))