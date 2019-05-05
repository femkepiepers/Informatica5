def gift_inschrijven(klas, totaal):

    if klas[0] in totaal:
        totaal[klas[0]] += klas[1]
    else:
        totaal[klas[0]] = klas[1]

    return totaal