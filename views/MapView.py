import pygame
from pygame.locals import *
from views.HexTileView import HexTileView

class MapView:
    def __init__(self, surface, map_model, size=100):
        self.surface = surface
        self.map = map_model
        self.size = size

    def draw(self):
        top_left_tile = list(self.map.map.keys())[0]        #get the tile that was generated first (top left tile) for reference
        for cube, info in self.map.map.items():
            tile = HexTileView(self.size, cube, info, top_left_tile)
            self.surface.blit(tile.image, tile.position)
