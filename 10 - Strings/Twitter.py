# invoer
tweet = str(input('Tweet: '))
mes = ''

# bewerkingen
for i in range(0, len(tweet)):
    if tweet[i] == '#':
        b = tweet[i:].find(' ')
        if (b + i) > i:
            mes = tweet[i + 1:i + b]
            print(mes)
