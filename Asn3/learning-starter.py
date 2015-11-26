import mountaincar
from Tilecoder import numTilings, tilecode, numTiles
from Tilecoder import numTiles as n
from pylab import *  #includes numpy
import random

numRuns = 1
numEpisodes = 200
alpha = 0.5/numTilings #was originally 005/numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTiles * 3
F = [-1]*numTilings

runSum = 0.0
for run in xrange(numRuns):
    theta = -0.01*rand(n) 
    eTrace = [0]*n

    returnSum = 0.0
    for episodeNum in xrange(numEpisodes):
        G = 0
        delta = 0
        #your code goes here (20-30 lines, depending on modularity)
        state = mountaincar.init()

        while state != None:

            tiles = tilecode(state[0], state[1],[-1]*numTilings)
            explore = (random.random() <= epsilon)

            if explore:
                action = random.randint(0,2)
                reward, newState = mountaincar.sample(state, action)
            else:
                action = getBestAction(tiles, theta)
                reward, newState = mountaincar.sample(state, action)
            G += reward

            delta = reward + updateDelta(tiles, theta, action, state)
            eTrace = updateETrace(eTrace, tiles, action)
            theta = updateTheta(theta, delta, eTrace)

            state = newState


        print "Episode: ", episodeNum, "Steps:", step, "Return: ", G
        returnSum = returnSum + G
    print "Average return:", returnSum/numEpisodes
    runSum += returnSum
print "Overall performance: Average sum of return per run:", runSum/numRuns

def updateDelta(tiles,theta, action, state):
    nextTiles = tilecode(state[0], state[1],[-1]*numTilings)
    if i in nextTiles:
        delta += (1/3)*theta[i]
        delta += (1/3)*theta[i + 4*81]
        delta += (1/3)*theta[i + 8*81]
    if i in tiles:
        delta -= theta[i + action*4*81]
    return delta

def updateTheta(theta,delta, eTrace):
    oldTheta = theta
    for i in range(len(theta)):
        theta[i] = oldTheta[i] + (alpha*delta*eTrace[i])
    return theta

def updateETrace(eTrace, tiles, action):
    oldETrace = eTrace
    for i in range(len(eTrace)):
        if (i + action*4*81) in tiles:
            eTrace[i] = 1
        else:
            eTrace[i] = lmbda*oldETrace[i]
    return eTrace

def getBestAction(tiles, theta):
    actions = [0] * 3
    for i in range(len(theta)):
        if i in tiles:
            actions[0] += theta[i]
            actions[1] += theta[i + 4*81]
            actions[2] += theta[i + 2*4*81]    
    return actions.index(max(actions))   

#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data
def writeF():
    fout = open('value', 'w')
    F = [0]*numTilings
    steps = 50
    for i in range(steps):
        for j in range(steps):
            tilecode(-1.2+i*1.7/steps, -0.07+j*0.14/steps, F)
            height = -max(Qs(F))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()


