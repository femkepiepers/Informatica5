# elke letter verschuift n letters in het ASCII-tabel
# indien de nieuwe letter een @ is, verander dan het teken naar een spatie

def versleutel_woord(woord, n):
    code = ''
    woord = woord.upper()
    for letter in woord:
        code_letter = chr(ord(letter) + n)

        if code_letter == '@':
            code_letter = ' '

        code_letter += code_letter

    return code

# elke woord in de zin wordt versleuteld.
def versleutel_zin(zin, getal):

    index_spatie = zin.find()
    code = ''

    while index_spatie != -1:
        woord = zin[:index_spatie]
        zin = zin[index_spatie + 1:]

        code += '@' + versleutel_woord(woord, getal)
        index_spatie = zin.find(' ')

    if len(zin) > 0:
        code += '@' + versleutel_woord(zin, getal)

    return code