from Cube import Cube 

class HexMap:
    def __init__(self):
        self.map = {} 
   
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
    hex_map = HexMap()
    origin_cube = Cube(0,0,0)
    hex_map[origin_cube] = {"player":False, "tile":"grass"}
    count = 0
    for cube in hex_map.cube_neighbour(origin_cube):
        hex_map[cube] = {"player":False, "tile": "water","count": count}
        print(hex_map[cube])
        print(cube.x,cube.y,cube.z)
        count += 1
    print(hex_map[Cube(0,0,0)])
    print(hex_map[Cube(0,1,-1)])
    print(hex_map[Cube(1,0,-1)])
    print(hex_map[Cube(1,-1,0)])
    print(hex_map[Cube(0,-1,1)])
    print(hex_map[Cube(-1,0,1)])
    print(hex_map[Cube(-1,1,0)])

    print(len(hex_map.map))
    
        

    
