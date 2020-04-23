from models.Cube import Cube 

class HexMap:
    def __init__(self, map_dict={}):
        for k in map_dict.keys():
            if not isinstance(k, Cube):
                raise ValueError(f"HexMap only accepts Cube object as key, but instead got {type(k)}")
        self.map = map_dict
   
    def __getitem__(self, key):
        return self.map[key]
    
    def __setitem__(self, key, value):
        self.map[key] = value

    def generate(self, px, py, pz, nx, ny, nz):
        pass
    
    def export_map(self):
        pass
    
    @classmethod
    def convert_map(cls, data):
        pass
    
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

if __name__ == '__main__':
    x = HexMap()
    start_tile = Cube(0,0,0)
    dist = 3
    tiles = x.cube_neighbour(start_tile,dist)
    for r in range(1,dist+1):
        print(f'Ring {r}')
        print('*'*20)
        itr = 0
        for tile in tiles:
            if max(abs(tile.x),abs(tile.y),abs(tile.z)) == r:
                print(tile.x,tile.y,tile.z)
                itr += 1
        print(f'Tiles in ring {r} = {itr}\n')

