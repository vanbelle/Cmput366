numTilings = 8
offset = 0.6/numTilings

#tile code takes 2 numbers (x,y) and translates them into the tile number 
#in which the numbers land after each tiling.
def tilecode(x,y,tileIndices):
    #finding the tile corresponding to the vectors is repeated 8 times  
    for i in range(0,numTilings):
        # row/column are determined by adding i*offset to the tiling index to repersent the 
        # matrix offset and then dividing by 0.6 (the width per tile) to determine the row or column
        column = (x + i*offset) // 0.6
        row = (y + i*offset) // 0.6 
        # the tile number is found using a base number i*121 to show which tiling we are on, and then 
        # adding column*10 and row to bring us to the tile within a particular tiling 
        tile = (i*121) + (11*column) + row
        tileIndices[i] = int(tile)
    return tileIndices    
    
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tileIndices = tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
    
