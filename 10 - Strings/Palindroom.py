def is_palindroom(woord):
    a = len(woord)
    boodschap = ''
    if a == 1:
        boodschap = True
    else:
        for i in range(0, (a // 2)):
            if woord[i] == woord[a - 1 - i] and boodschap != False:
                boodschap = True
            else:
                boodschap = False
    return boodschap