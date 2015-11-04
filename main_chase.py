from __future__ import division
import blackjack
import random
from random import randint


#== Globals
Q = [[0 for x in range(2)]for x in range(181)]
numEpisodes = 11000000
alpha = 0.001
gamma = 1
epsilon = 0.001

S = 0
returnSum = 0

def avg(Q):
	sum = 0
	for i in range(len(Q)):
		for j in range(len(Q[i])):
			sum += Q[i][j]
	return sum / (len(Q) * 2)


#initialize Q to small random number
for i in range(len(Q)):
	for j in range(len(Q[i])):
		Q[i][j] = random.random() * 0.001

#== Main
for episodeNum in range(numEpisodes):
	S = blackjack.init()
	G = 0

	#while S is not in terminal state
	while S != -1:


		#Choose action here based on epsilon
		decider = random.random()
		if decider <= epsilon:
			A = randint(0,1)
		else:
			# A = the best action to take
			if Q[S][0] >= Q[S][1]:
				A = 0
			else:
				A = 1

		R,Sprime = blackjack.sample(S,A)
		G = G + R

		#print str(Sprime)+":"+str(A)

		if Sprime == -1:
			Q[S][A] = Q[S][A] + alpha*(R - Q[S][A])	
		else:
			#if decider <= epsilon:
			#	Q[S][A] = Q[S][A] + alpha*(R + gamma*(0.5 * Q[Sprime][0] + 0.5 * Q[Sprime][1]) - Q[S][A])
			#else:
			Q[S][A] = Q[S][A] + alpha*(R + gamma*(max(Q[Sprime][0],Q[Sprime][1])) - Q[S][A])
		
		S = Sprime

	if episodeNum == 1000000:
		print "==============================================="
		epsilon = 0

	if episodeNum % 10000 == 0:
		#print "Episode: " + str(episodeNum) + " Return: " + str (G)
		print "Current Avg: " + str(returnSum / (episodeNum+1)) + "Ep: " + str(episodeNum)
	returnSum = returnSum + G



print "Avg Return:" + str(returnSum / numEpisodes)
	#
		#print "Avg Return: " + str(returnSum/(episodeNum+1))

	
	

def printActionValues(Q):
	print("Action Values:")
	for S in range(181):
		print str(blackjack.visualDecode(S)) + " Stay: " + str(Q[S][0])
		print str(blackjack.visualDecode(S)) + " Hit: " + str(Q[S][1])


def printPolicy(Q):
	print "policy: "
	for S in range(181):
		if Q[S][0] >= Q[S][1]:
			print str(blackjack.visualDecode(S)) + " Stay"
		else:
			print str(blackjack.visualDecode(S)) + " Hit"


#printPolicy(Q)
