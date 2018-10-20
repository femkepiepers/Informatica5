# invoer
speler_1 = input('Speler 1: ')
speler_2 = input('Speler 2: ')

# uitvoer
if speler_1 == 'blad':
    if speler_2 == 'steen':
        print('speler 1 wint')
    if speler_2 == 'schaar':
        print('speler 2 wint')
if speler_1 == 'steen':
    if speler_2 == 'schaar':
        print('speler 1 wint')
    if speler_2 == 'blad':
        print('speler 2 wint')
if speler_1 == 'schaar':
    if speler_2 == 'blad':
        print('speler 1 wint')
    if speler_2 == 'steen':
        print('speler 2 wint')
if speler_1 == speler_2:
    print('onbeslist')