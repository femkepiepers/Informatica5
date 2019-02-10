def ik_heb_gemoord(opdrachten, persoon):
    opdracht = []
    plaats = opdrachten.index(persoon)

    if len(opdrachten) == 1:
        opdracht = opdrachten[0]

    elif len(opdrachten) > 1:

        if plaats + 1 < len(opdrachten):
            opdrachten.pop(plaats + 1)
        else:
            opdrachten.pop(0)

        if plaats + 1 < len(opdrachten):
            opdracht = opdrachten[plaats + 1]
        else:
            opdracht = opdrachten[0]

    return opdracht, opdrachten


def ik_ben_vermoord(lijst, slachtoffer):
    plaats_persoon = lijst.index(slachtoffer) - 1

    persoon = lijst[plaats_persoon]

    opdracht = ik_heb_gemoord(lijst, persoon)
    opdrachten = ik_heb_gemoord(lijst, persoon)

    return opdracht, opdrachten