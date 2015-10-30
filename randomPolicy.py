import blackjack
from pylab import *
from random import randint

numEpisodes = 2000

returnSum = 0.0
for episodeNum in range(numEpisodes):
    G = 0
    S = blackjack.init()

    while S != -1:
   		R, Sprime = blackjack.sample(S, randint(0,1))
		G = G + R
		S = Sprime

    print "Episode: ", episodeNum, "Return: ", G
    returnSum = returnSum + G
print "Average return: ", returnSum/numEpisodes
