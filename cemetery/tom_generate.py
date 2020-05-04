from HexMap import HexMap
from Cube import Cube

class GenMap(HexMap):
    def __init__(self, map_dict={}):
        super().__init__(map_dict)

# Generates anal bead map if my math is correct. 
# shifts so only one cube is shared between regions. 
    def generate(self, dist, regions=1):
        for region in range(regions):
            shift = dist * region * 2
            origin_cube = Cube(0,0+shift,0-shift)
            cubes = self.cube_neighbour(origin_cube, dist)
            cubes.insert(0,origin_cube)
            for cube in cubes:
                self.map[cube] = f"cube={cube} region={region}"
        return


if __name__ == '__main__':
    x = GenMap()
    x.generate(1,2)
    for v in x.map.values():
        print(v)
    print("number of cubes in map:", len(x.map))
