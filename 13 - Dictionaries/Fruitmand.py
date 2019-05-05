def fruitmand_maken(totaal):

    mand = {}
    for item in totaal:

        if len(item) not in mand.keys():
            mand[len(item)] = item

        else:
            vorig = mand[len(item)]
            if totaal.count(item) >= totaal.count(vorig):
                mand.pop(len(item))
                mand[len(item)] = item

    return mand

def fruitmand_inpakken(totaal):

    fruit = []
    while len(totaal) != 0:
        vorige = min(totaal.keys())
        fruit.append(totaal[vorige])
        totaal.pop(vorige)

    return fruit
