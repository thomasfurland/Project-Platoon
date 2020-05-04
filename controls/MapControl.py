from models.HexMap import HexMap
from models.Cube import Cube
from views.MapView import MapView
from models.evan_generate import MapGen

class MapControl:
    def __init__(self, surface):
        self.surface = surface
        self.map_model = self.create_map_evan()

    def create_map_evan(self):
        genner = MapGen()
        genner.generator(11,15)
        return genner

    def create_map_thomas(self):
        origin_cube = Cube(0, 0, 0)
        hex_map = HexMap() 
        cubes = hex_map.cube_neighbour(origin_cube)
        cubes.append(origin_cube)
        shift = 0
        for cube in cubes:
            hex_map[cube] = {"color": (0, 0, 25*shift)}
            shift += 1
        print([(cube, cube.offset_x, cube.offset_y) for cube in cubes])
        return hex_map

    def draw_map(self):
        map_view = MapView(self.surface, self.map_model)
        map_view.draw()
        return
