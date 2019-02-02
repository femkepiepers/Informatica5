def vlag(richting, kleuren):

    if richting == 'verticaal':
        a = len(kleuren)
        mes = ''
        for i in range(0, a + 1):
            mes += kleuren[i] + ' | '
            if i == a:
                mes += kleuren[i]

        return mes

   # elif richting == 'horizontaal':
    #    for i in range(0, len(kleuren)):
     #       mes = kleuren[i] + '\n' + '-' + '\n'

      #  return mes


print(vlag('verticaal',('rood', 'wit', 'blauw')))