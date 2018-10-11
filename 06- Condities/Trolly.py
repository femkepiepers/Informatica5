# invoer
hendel_trekken = input('Trek aan de hendel van de wissel? (ja/nee) ')
man_van_brug = input('Man van brug duwen? (ja/nee) ')

# uitvoer
if hendel_trekken == 'ja' and man_van_brug == 'ja':
    print('2')

if hendel_trekken == 'ja' and man_van_brug == 'nee':
    print('1')

if hendel_trekken == 'nee' and man_van_brug == 'ja':
    print('1')

if hendel_trekken == 'nee' and man_van_brug == 'nee':
    print('5')