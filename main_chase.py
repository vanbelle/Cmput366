import blackjack
from random import randint

#== Globals
Q = [[0 for x in range(2)]for x in range(181)]
alpha = 0.5
gamma = 1
numEpisodes = 2000

S = 0


#== Main
for episodeNum in range(numEpisodes):
	print "Starting Epsisode " + str(episodeNum)
	S = blackjack.init()

	#while S is not in terminal state
	while S != -1:
		A = randint(0,1)
		R,Sprime = blackjack.sample(S,A)

		print str(Sprime)+":"+str(A)

		if Sprime == -1:
			Q[S][A] = Q[S][A] + alpha*(R - Q[S][A])	
		else:
			Q[S][A] = Q[S][A] + alpha*(R + gamma*(0.5 * Q[Sprime][0] + 0.5 * Q[Sprime][1]) - Q[S][A])

		S = Sprime
		
	
	print "[*] Terminal State Reached"
	print ""

print "Action Value functions: "
for S in range(181):
	print str(blackjack.visualDecode(S)) + " Stay: " + str(Q[S][0])
	print str(blackjack.visualDecode(S)) + " Hit: " + str(Q[S][1])




