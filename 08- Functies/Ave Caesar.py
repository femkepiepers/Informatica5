def is_letter(n):
    if n in 'abcdefghijklmnopqrstuvwxyz' or n in'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        boodschap = True
    else:
        boodschap = False
    return boodschap

def roteer_letter(a, b):
    if a in 'abcdefghijklmnopqrstuvwxyz':
        if(ord(a) + b) > ord('z'):
            c = (ord(a) + b) - ord('z')
            letter = chr(ord('a') - 1 + c)
        else:
            letter = chr(ord(a) + b)
    else:
        if (ord(a) + b) > ord('Z'):
            c = (ord(a) + b) - ord('Z')
            letter = chr(ord('A') - 1 + c)
        else:
            letter = chr(ord(a) + b)
    return letter

def versleutel(a, b):
    boodschap = a
    nieuwe_boodschap = ''
    for letter in boodschap:
        if is_letter(letter) == True:
            nieuwe_letter = roteer_letter(letter, b)
            nieuwe_boodschap += nieuwe_letter
        else:
            nieuwe_boodschap += letter
    return nieuwe_boodschap