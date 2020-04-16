from Cube import Cube 

class HexMap:
    def __init__(self):
        self.map = {}

    def generate(self, px, py, pz, nx, ny, nz):
        for x in range(nx,px):
            for y in range(ny,py):
                for z in range(nz,pz):
                    cube = Cube(x, y, z)
                    self.map[cube] = f"x:{x} y:{y} z:{z}"
    
    
if __name__ == '__main__':
    hex_map = HexMap()
    hex_map.generate(2, 2, 2, -2, -2, -2)
    print(hex_map.map)
    print(len(hex_map.map))
    
        

    
