tweet : input('geef tweet: ')

i_hashtag = tweet.find('#')
# zolang als er # zijn
while i_hashtag != -1:
    # tweet afknippen na het #-teken
    tweet = tweet[i_hashtag + 1:]
    i_spatie = tweet.find(' ')

    # hashtag uitknippen ( en printen )
    print(tweet[:i_spatie])

    # tweet inkorten (1e # is al weg dus hoeft niet meer per se)
    # terug op zoek naar een #
    i_hashtag = tweet.find('#')

