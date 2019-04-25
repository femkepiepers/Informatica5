#bestand = open('Klas.txt')

#lijn = bestand.readline()

#while lijn != '':
    #print(lijn)
    #lijn = bestand.readline()

#bestand.close()

# lijnen = []
#
# with open('Klas.txt') as bestand:
#     lijnen = bestand.readlines()
#
# print('er zitten ' + str(len(lijnen)) + ' personen in de klas')

nieuwe_leerlingen = ['Alice', 'Baptiste']

with open('Klas.txt', 'w') as bestand:
    bestand.write('\n' + '\n'.join(nieuwe_leerlingen))
# a is write en r is lees
with open('Klas.txt', 'w') as bestand:
    bestand.writelines(''.join(nieuwe_leerlingen))