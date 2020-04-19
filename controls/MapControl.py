from models.HexMap import HexMap
from models.Cube import Cube
from views.MapView import MapView

class MapControl:
    def __init__(self, surface):
        self.surface = surface
        self.map_model = self.create_map()
        
    def create_map(self):
        origin_cube = Cube(0, 0, 0)
        hex_map = HexMap() 
        cubes = hex_map.cube_neighbour(origin_cube)
        cubes.append(origin_cube)
        shift = 0
        for cube in cubes:
            hex_map[cube] = {"color": (0, 0, 25*shift)}
            shift += 1
        return hex_map

    def draw_map(self):
        map_view = MapView(self.surface, self.map_model)
        map_view.draw()
        return
