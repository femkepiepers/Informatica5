def vlag(richting, kleuren):

    if richting == 'verticaal':
        mes = ''
        for i in range(0, len(kleuren)):
            mes += kleuren[i]
            if i != len(kleuren) - 1:
                mes += ' | '
    elif richting == 'horizontaal':
        mes = ''
        for i in range(0, len(kleuren)):
            mes += kleuren[i]
            if i != len(kleuren) - 1:
                mes += '\n' + '-' + '\n'

    return mes

print(vlag('verticaal',('rood', 'wit', 'blauw')))