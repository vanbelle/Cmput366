## HOW IT WORKS ############################################################################
## Uses tilecoder to learn.
## See f(x,y) and learn(x,y,target) for the meat of what's going on.
##
## Modified by Chase McCarty and Sarah Van Belleghem in 2015
############################################################################################

from pylab import zeros, sin, cos, normal, random
from Tilecoder import numTilings, tilecode

# initialize weights appropriately here
theta = [0] * 968
# initialize step size parameter appropriately here
alpha = 0.1/numTilings
# initialize your global list of tile indices here
phi = [0] * 968
    
# Returns what AI's estimate f(x,y) = z 
# Finds the "numTiles" tiles corresponding to the given x,y
# Each tile makes up 1/"numTiles" the value of the estimated z. 
# Sum up the 8 theta values, and return the estimated z
def f(x,y):
    # write your linear function approximator here (5 lines or so)
    total = 0
    vectorLength = len(theta) # corresponds to n in the algorithm
    featureVectorArray = tilecode(x,y,[-1]*numTilings)
    for i in range(vectorLength):
        if i in featureVectorArray: 
            total += theta[i] 
    return total
   
# is given a sample x,y and true z for f(x,y) = x.
# Grabs the "numTiles" tiles corresponding to the given x and y.
# moves each theta corresponding to a tile alpha/"numTilings" closer to the
# true value it should be
def learn(x,y,target):
    # write your gradient descent learning algorithm here (3 lines or so)
    featureVectorArray = tilecode(x,y,[-1]*numTilings)
    for i in range(len(theta)):
        if i in featureVectorArray:
            theta[i] = theta[i] + alpha*(target - f(x,y))


def test1():
   for x,y,target in \
         [ (0.1, 0.1, 3.0), \
           (4.0, 2.0, -1.0), \
           (5.99, 5.99, 2.0), \
           (4.0, 2.1, -1.0) ]:
        before = f(x,y)
        learn(x,y,target)
        after = f(x,y)
        print 'Example (', x, ',', y, ',', target, '):'
        print '    f before learning: ', before, 
        print '    f after learning : ', after
    
def targetFunction(x,y):
    return sin(x-3.0)*cos(y) + normal(0,0.1)

#Is given the number of sample sets to generate. 
#Generates a new true z, and calls learn with it
def train(numSteps):
    for i in range(numSteps):
        x = random() * 6.0
        y = random() * 6.0
        target = targetFunction(x,y)
        learn(x,y,target)
    
def writeF(filename):
    fout = open(filename, 'w')
    steps = 50
    for i in range(steps):
        for j in range(steps):
            target = f(i * 6.0/steps, j * 6.0/steps)
            fout.write(repr(target) + ' ')
        fout.write('\n')
    fout.close()

# Uses sampleSize iterations random values of x and y, to compare
# the value of our estimates
def MSE(sampleSize):
    totalSE = 0.0
    for i in range(sampleSize):
        x = random() * 6.0
        y = random() * 6.0
        error = targetFunction(x,y) - f(x,y)
        totalSE = totalSE + error * error
    print 'The estimated MSE: ', (totalSE / sampleSize)
    
def test2():
    train(20)
    writeF('f20')
    MSE(10000)
    for i in range(10):
        train(1000)
        MSE(10000)
    writeF('f10000')

test1()

