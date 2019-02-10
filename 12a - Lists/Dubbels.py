def dubbels(lijst):
    lijst_dubbels = []
    i = 0
    while i < len(lijst):

        for item in lijst:

            if lijst.count(item) > 1 and item not in lijst_dubbels:
                lijst_dubbels.append(item)
            elif item == '[]':
                return '[]'

            return lijst_dubbels
        i += 1

print(dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris']))