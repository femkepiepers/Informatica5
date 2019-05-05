def synoniemen(tekst, synoniemen):

    tekst = tekst.split()

    for i in range(len(tekst)):
        if tekst[i] in synoniemen:
            tekst[i] = synoniemen.get(tekst[i])

    tekst = ' '.join(tekst)

    return tekst