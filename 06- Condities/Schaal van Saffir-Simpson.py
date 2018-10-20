# invoer
windsnelheid = input('De windsnelheid bedraagt: ')

# uitvoer
if windsnelheid < '119':
    print('geen orkaan')

if windsnelheid >= '119' and windsnelheid <= '153':
    print('categorie 1')

if windsnelheid >= '154' and windsnelheid <= '177':
    print('categorie 2')

if windsnelheid >= '178' and windsnelheid <= '209':
    print('categorie 3')

if windsnelheid >= '210' and windsnelheid <= '249':
    print('categorie 4')

if windsnelheid >= '250':
    print('categorie 5')
