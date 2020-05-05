import pygame
from pygame.locals import *
from views.HexTileView import HexTileView

class MapView:
    def __init__(self, surface, map_model, size=100):
        self.surface = surface
        self.map = map_model
        self.size = size

    def draw(self):
        for cube, info in self.map.map.items():
            tile = HexTileView(self.size, cube, info)
            self.surface.blit(tile.image, tile.position)
