from pygame import Surface
from models.HexMap import HexMap
from views.HexTileView import HexTileView

class Renderer:
    def __init__(self, window):
        self.surface = window._surface
        self.size = 100 #can be passed in as a value to enable zooming
        self.map = HexMap()
    
    def render_map(self):
        for cube, info in self.map.map.items():
            tile = HexTileView(self.size, cube, info)
            self.surface.blit(tile.image, tile.position)


