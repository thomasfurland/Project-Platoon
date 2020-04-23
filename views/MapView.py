import pygame
from pygame.locals import *

class MapView:
    def __init__(self, surface, map_model):
        self.surface = surface
        self.map = map_model

    def draw(self):
        shift = 0
        for value in self.map.map.values():
            tile = pygame.Rect(50*shift, 50*shift, 50, 50)
            pygame.draw.rect(self.surface, value["color"], tile)
            shift += 1
