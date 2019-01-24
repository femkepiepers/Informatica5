def versleutel_woord(woord, n):
    # alle letters overlopen
    for i in range(0, len(woord) + 1):

        # kleine letters vervangen door hoofdletters
        if woord[i] in 'abcdefghijklmnopqrstuvwxyz':
            woord[i].upper()

        # het teken veranderen door het teken dat n plaatsen verder staat in de ASCII-tabel
        elif woord[i] in woord:
            woord.replace('woord[i]', 'chr(ord('woord[i]') + n)')

            # elk apenstaartje vervangen door een spatie
            if ord('woord[i]') == 64:
                woord.replace('chr(64)', 'chr(32)')

    return woord

def versleutel_zin(zin):

    for i in range(0, len(zin) + 1):
        if zin[i] in 'abcdefghijklmnopqrstuvwxyz':
            zin[i].upper()

        elif zin[i] in zin:
            a = ord('zin[i]') + n
            zin.replace('zin[i]', 'chr(a)')

        elif ord('zin[i]') == 64:
            zin.replace('chr(64)', 'chr(32)')

        elif zin[i] == ' ':
            zin.replace(' ', '@')
    return zin


