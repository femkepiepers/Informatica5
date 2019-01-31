def vlag(richting, kleuren):

    if richting == 'verticaal':
        mes = kleuren[0] + ' | ' + kleuren[1] + ' | ' + kleuren[2]
        return mes

    elif richting == 'horizontaal':
        mes = kleuren[0]
        a = 0
        while a < len(kleuren) + 1:
            a += 1
            mes += ' - '
            mes += kleuren[a]

        return mes

print(vlag('horizontaal',('rood', 'wit', 'blauw')))