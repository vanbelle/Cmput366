## HOW IT WORKS ############################################################################
#   takes 2 numbers, x and y, and translates them 
#   into their corresponding tile number in each tiling. 
#   Because there are 8 tilings, it returns 8 values (the 
#   tile corresponding to x,y in each tiling)
#
#   to determine these tiles:
#   for each tile coding, the the tile is 
#   (x and y + the current offset) / 0.6 and then rounded down 
#   to whole numbers
#
#   what this does, is puts very similar input together on some 
#   tiles but not all tiles. for example see samples 2, and 4 in this output
#
#   Tile indices for input ( 0.1 , 0.1 ) are :  [0, 121, 242, 363, 484, 605, 726, 859]
#   Tile indices for input ( 4.0 , 2.0 ) are :  [69, 190, 311, 443, 564, 685, 807, 928]
#   Tile indices for input ( 5.99 , 5.99 ) are :  [108, 241, 362, 483, 604, 725, 846, 967]
#   Tile indices for input ( 4.0 , 2.1 ) are :  [69, 190, 311, 443, 565, 686, 807, 928]
#
#   Modified by Chase McCarty and Sarah Van Belleghem in 2015
############################################################################################

numTilings = 4
numTiles = numTilings*81
roffset = 0.175 / numTilings
coffset = 0.225 / numTilings 

#tile code takes 2 numbers (x,y) and translates them into the tile number 
#in which the numbers land after each tiling.
def tilecode(x,y,tileIndices):
    #finding the tile corresponding to the vectors is repeated 8 times
    x += 1.2
    y += 0.7  
    for i in range(0,numTilings):
        # row/column are determined by adding i*offset to the tiling index to repersent the 
        # matrix offset and then dividing by 0.6 (the width per tile) to determine the row or column
        column = (x + i*coffset) // 0.225
        row = (y + i*roffset) // 0.175
        # the tile number is found using a base number i*121 to show which tiling we are on, and then 
        # adding column*10 and row to bring us to the tile within a particular tiling 
        tile = (i*81) + (9*column) + row
        tileIndices[i] = int(tile)
    return tileIndices    
    
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tileIndices = tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

#printTileCoderIndices(0.1,0.1)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)
#printTileCoderIndices(-1.2, -0.7)    
