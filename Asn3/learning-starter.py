from __future__ import division
import mountaincar
from Tilecoder import numTilings, tilecode, numTiles
from Tilecoder import numTiles as n
from pylab import *  #includes numpy
import random

numRuns = 1
numEpisodes = 1000
alpha = 0.5/numTilings #was originally 005/numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTiles * 3
F = [-1]*numTilings

def getBestAction(tiles, theta):
    actions = [0] * 3
    for i in range(numTiles):
        if i in tiles:
            actions[0] += theta[i]
            actions[1] += theta[i + 4*81]
            actions[2] += theta[i + 2*4*81]    
    return (actions.index(max(actions))) 

def updateDelta(tiles, theta, action, newState):
    nextTiles = tilecode(newState[0], newState[1],[-1]*numTilings)
    delta = 0
    nextAction = getBestAction(nextTiles, theta)
    for i in nextTiles:
        delta += theta[i + nextAction*4*81]
    for i in tiles:
        delta -= theta[i + action*4*81]
    return delta

def updateTheta(theta,delta, eTrace):
    oldTheta = theta[:]
    for i in range(len(theta)):
        theta[i] = oldTheta[i] + (alpha*delta*eTrace[i])
    return theta

def updateETrace(eTrace, tiles, action):
    oldETrace = eTrace[:]
    for i in range(len(eTrace)):
        eTrace[i] = lmbda*oldETrace[i]     
    for tile in tiles:
            eTrace[tile + action*4*81] = 1
    return eTrace 

def Qs(F):
    returnArray = []
    for i in F:
        returnArray.append(theta[i])
    return returnArray

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


def writeAvgReturn(averageArray):
    for i in range(len(averageArray)):
        print "Episode ", i, ": Return: ", averageArray[i][0], ", Steps: ", averageArray[i][1]

runSum = 0.0

## Learning Curve
numRuns = 1 
numEpisodes = 1000
averageArray = [(0,0)]*numEpisodes ## tuple ordered (return, steps)
## =======================

for run in xrange(numRuns):
    theta = -0.01*rand(n) 
    returnSum = 0.0
    #stepSum = 0
    print "Run: ", run
    for episodeNum in xrange(numEpisodes):
        eTrace = [0]*n
        G = 0
        delta = 0

        state = mountaincar.init()
        step = 0
        while state != None:
            step += 1

            tiles = tilecode(state[0], state[1],[-1]*numTilings)
            explore = (random.random() < epsilon)

            if explore:
                action = random.randint(0,2)
                reward, newState = mountaincar.sample(state, action)
            else:
                action = getBestAction(tiles, theta)
                reward, newState = mountaincar.sample(state, action)
            G += reward

            if newState != None:
                delta = reward + updateDelta(tiles, theta, action, newState)
                eTrace = updateETrace(eTrace, tiles, action)
                theta = updateTheta(theta, delta, eTrace)
            else:
                Qa = 0
                for i in tiles:
                    Qa += theta[i + action*4*81]
                delta = reward - Qa
                updateETrace(eTrace, tiles, action)
                theta = updateTheta(theta, delta, eTrace)

            state = newState
        print "Episode: ", episodeNum, "Steps:", step, "Return: ", G
        returnSum = returnSum + G
        #stepSum = stepSum + step

        ## Learning Curve
        averageArray[episodeNum] = (averageArray[episodeNum][0] + G, averageArray[episodeNum][1] + step)
        ## ========================

    print "Average return:", returnSum/numEpisodes
    runSum += returnSum
print "Overall performance: Average sum of return per run:", runSum/numRuns

## Learning Curve
## Average out learning curve
for i in range(len(averageArray)):
    averageArray[i] = (averageArray[i][0]/50, averageArray[i][1]/50)
writeAvgReturn(averageArray)
## ========================

##writeF()
