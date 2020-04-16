from Cube import Cube 

class HexMap:
    def __init__(self, map_dict={}):
        for k in map_dict.keys():
            if not isinstance(k, Cube):
                raise ValueError(f"HexMap only accepts Cube as key, bug got {k}")
        self.map = map_dict
   
    def __getitem__(self, key):
        return self.map[key]
    
    def __setitem__(self, key, value):
        self.map[key] = value

    def generate(self, px, py, pz, nx, ny, nz):
        pass
    
    def export(self):
        pass
    
    @classmethod
    def import_map(cls, data):
        pass

    def cube_neighbours(self, cube):
        neighbours = [
            Cube(cube.x, cube.y+1, cube.z-1),
            Cube(cube.x+1, cube.y, cube.z-1),                    
            Cube(cube.x+1, cube.y-1, cube.z),
            Cube(cube.x, cube.y-1, cube.z+1),
            Cube(cube.x-1, cube.y, cube.z+1),                   
            Cube(cube.x-1, cube.y+1, cube.z)
        ]
        return neighbours

if __name__ == '__main__':
    x = HexMap(map_dict={Cube(1, 0, -1): 10})