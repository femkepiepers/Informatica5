def bereken_prijs(boodschap):
    mes = ''
    for i in range(0, len(boodschap) + 1):
        if boodschap[i] == '<':
            a = boodschap.find('>')
            if a > i:
                mes += boodschap[0:i - 1] + ',' + boodschap[i + 1:a - 1] + boodschap[-1]
    return mes
print(bereken_prijs('I spent my last money on this billboard. Please give me a job.<2.68>'))