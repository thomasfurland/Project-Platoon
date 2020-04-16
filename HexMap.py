from Cube import Cube 

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

    def cube_neighbour(self, cube):
        xOffset = [-1,0,1]
        yOffset = [-1,0,1]
        neighbors = []
        for i in xOffset:
            for j in yOffset:
                if not(i == 0 and j == 0):
                    k = -(i+j)
                    if k**2 <= 1:
                        neighbors.append(Cube(cube.x+i,cube.y+j,cube.z+k))
        return neighbors

if __name__ == '__main__':
    x = HexMap(map_dict={(1, 0, -1): 10})
