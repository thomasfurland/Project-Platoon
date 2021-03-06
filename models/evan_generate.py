import math as m
from Cube import Cube
from HexMap import HexMap
#Note that both map length and width must be odd numbers

class MapGen(HexMap):
    def __init__(self,map_dict={}):
        super().__init__(map_dict)

    def generator(self,height,width):
        z_max = m.floor(height/2)
        y_mid = m.floor(width/2)
        for z in range(-z_max,z_max+1):    #start it at the positive top x_max, going down to -x_max
            if z % 2 == 0:
                for y in range(int(y_mid - z/2),int(-y_mid - z/2)-1,-1): # go left to right, which is positive to negative ###also updated so that it's minus
                    x = -(z+y)
                    self.map[Cube(x,y,z)] = f'{x},{y},{z}'
            if z % 2 == 1:
                for y in range(int(y_mid - (z+1)/2),int(-y_mid - (z+1)/2)-1,-1): #also go left to right
                    x = -(z+y)
                    self.map[Cube(x,y,z)] = f'{x},{y},{z}'

if __name__ == '__main__':
    genner = MapGen()
    genner.generator(5,7)
    for tile in genner.map.values():
        print(tile)