# invoer
p_1 = input('Persoon 1 draagt: ')
p_2 = input('Persoon 2 draagt: ')
omg_antwoord = input('Welke persoon antwoord omgekeerd? ')

# uitvoer
if p_1 == 'zwart' and p_2 == 'zwart' and omg_antwoord == '1' or p_1 == 'wit' and p_2 == 'wit' and omg_antwoord == '2':
    print('wit')
    print('zwart')
if p_1 == 'zwart' and p_2 == 'wit' and omg_antwoord == '1' or p_1 == 'wit' and p_2 == 'zwart' and omg_antwoord == '2':
    print('zwart')
    print('zwart')
if p_1 == 'zwart' and p_2 == 'zwart' and omg_antwoord == '2' or p_1 == 'wit' and p_2 == 'wit' and omg_antwoord == '1':
    print('zwart')
    print('wit')
if p_1 == 'zwart' and p_2 == 'wit' and omg_antwoord == '2' or p_1 == 'wit' and p_2 == 'zwart' and omg_antwoord == '1':
    print('wit')
    print('wit')