def dubbels(lijst):

    lijst_dubbels = []

    for item in lijst:

        if lijst.count(item) > 0 and item not in lijst_dubbels:
            lijst_dubbels.append(item)

    return lijst_dubbels

print