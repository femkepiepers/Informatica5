# invoer
woord = str(input('Verbrogen woord: '))
gedraaid_bedrag = int(input('Gedraaid bedrag: '))
letter = str(input('Letter: '))
totaal = 0
d = ''

# berekening
while letter in woord and letter not in d:
    totaal += gedraaid_bedrag
    d += letter
    letter = str(input('Letter: '))

if letter not in woord:
    totaal += 0

# uitvoer
print(totaal)