from models.HexMap import HexMap
from models.Cube import Cube
from controls.datagen import MapFactory

class GenMap(MapFactory):
    _unique_key = "Thomas"
    
    def __init__(self):
        super().__init__()
        self.map = HexMap()

    # Generates anal bead map if my math is correct. 
    # shifts so only one cube is shared between regions. 
    def generate(self, dist, regions=1):
        self.map.map = {}
        for region in range(regions):
            shift = dist * region * 2
            origin_cube = Cube(0,0+shift,0-shift)
            cubes = self.cube_neighbour(origin_cube, dist)
            cubes.insert(0,origin_cube)
            for cube in cubes:
                self.map[cube] = f"cube={cube} region={region}"
        return self.map

    #starting at bottom left hex 'dist' rings away from the center cube, iterates right to return hex in that row. does same for row above and repeats
    def cube_neighbour(self, cube,dist=1):
        xOffset = range(-dist,dist+1)
        yOffset = range(-dist,dist+1)
        neighbors = []
        for i in xOffset:
            for j in yOffset:
                if not(i == 0 and j == 0):
                    k = -(i+j)
                    if abs(k) <= dist:
                        neighbors.append(Cube(cube.x+i,cube.y+j,cube.z+k))
                        #could insert a bunch of stuff here and it will be preformed on every cube/hex inside the 'dist' ring
        return neighbors
