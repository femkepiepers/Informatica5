# invoer
aantal_lifters = int(input('Aantal lifters: '))
eindscore = 0
for i in range(aantal_lifters):
    score = float(input('Score: '))
    if i == score:
        eindscore = score
    elif score > eindscore:
        eindscore = score
    elif score < eindscore:
        eindscore = eindscore
# uitvoer
print(eindscore)