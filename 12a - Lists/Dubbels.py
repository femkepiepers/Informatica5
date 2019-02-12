def dubbels(lijst):
    lijst_dubbels = []

    for item in lijst:

        if lijst.count(item) > 1 and item not in lijst_dubbels:
            lijst_dubbels.append(item)

    return lijst_dubbels


print(dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris']))