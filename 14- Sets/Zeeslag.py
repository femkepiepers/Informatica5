def boot_overlappend(nieuwe, boot):
    mes = ''
    if nieuwe.isdisjoint(boot) == True:
        mes = False
    elif nieuwe.isdisjoint(boot) == False:
        mes = True
    return mes

def boot_toevoegen(nieuwe, boot):
    mes = ''
    if boot_overlappend(nieuwe, boot) == False:
        mes = boot.union(nieuwe)
    else:
        mes = boot
    return mes

def vuur(gok, boot):
    if gok in boot:
        mes = True
        boot.discard(gok)
    else:
        mes = False
    return mes, boot