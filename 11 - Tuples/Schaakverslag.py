def geldige_zet(wie, waarheen):

    if wie in 'KDTLP' and waarheen[0] in 'abcdefgh' and waarheen[1] in '12345678':
        mes = True

    elif waarheen[0] in 'abcdefgh' and waarheen[1] in '12345678':
        mes = True

    else:
        mes = False

    return mes

print(geldige_zet('LYKFB'))

wie = input('Wie: ')
aarheen = int(input('Waarheen: '))

if wie