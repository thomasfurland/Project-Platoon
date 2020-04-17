import math as m
from Cube import Cube
#both length and width must be odd numbers
map_tiles = []
def generator(height,width):
    x_max = m.floor(height/2)
    y_max = m.floor(width/2)
    for x in range(x_max,-x_max-1,-1):    #start it at the positive top x_max, going down to -x_max
        if x % 2 == 0:
            for y in range(int(y_max - x/2),int(-y_max - x/2)-1,-1): # go left to right, which is positive to negative
                z = -(x+y)
                map_tiles.append(Cube(x,y,z))
        if x % 2 == 1:
            for y in range(int(y_max - (x+1)/2),int(-y_max - (x+1)/2)-1,-1): #also go left to right
                z = -(x+y)
                map_tiles.append(Cube(x,y,z))

generator(7,7)
for tile in map_tiles:
    print(tile)