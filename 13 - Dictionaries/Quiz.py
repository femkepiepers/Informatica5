def verlaat_ploeg(naam, ploeg, inschrijvingen):

    if len(inschrijvingen[ploeg]) > 1:
        inschrijvingen[ploeg].remove(naam)

    else:
        inschrijvingen.pop(ploeg)

    return inschrijvingen

def vervoegt_ploeg(naam, ploeg, inschrijvingen):

    if ploeg in inschrijvingen:
        inschrijvingen[ploeg].append(naam)

    else:
        inschrijvingen[ploeg] = [naam]

    return inschrijvingen