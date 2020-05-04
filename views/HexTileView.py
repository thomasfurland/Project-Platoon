from pygame.sprite import Sprite
import math as m
from pygame import (
    Surface,
    init,
    display,
    draw,
    SRCALPHA
)

class HexTileView(Sprite):
    def __init__(self, size, cube, data, top_left_tile):
        super().__init__()
        self.width, self.height, self.r = m.ceil(size*0.5*(3**0.5)), size, size/2  #r is distance from center of hex to a corner
        self.center_w, self.center_h = self.width*0.5, self.height*0.5

        self.top_left_tile = top_left_tile      #again, used to reference each tile's position on the board relative to the corner
        self.cube = cube
        self.data = data
        self.image = Surface((self.width, self.height), SRCALPHA)
        self.rect = self.draw_hexagon()
        self.position = self.calculate_position()

    def draw_hexagon(self):
        hexagon_corners = self.calculate_corners()
        self.rect = draw.polygon(self.image, self.cube.colour, hexagon_corners)

    def calculate_position(self):
        w0 = (self.r)*(3**0.5)*(0.5)*(self.cube.x-self.top_left_tile.x-self.cube.y+self.top_left_tile.y+1)
        h0 = -(self.r)*(3)*(0.5)*(self.cube.x-self.top_left_tile.x+self.cube.y-self.top_left_tile.y-1)
        w = m.ceil(w0 - self.r*(3**0.5)/2)
        h = m.ceil(h0 - self.r)
        return w,h

    def calculate_corners(self):

        c1 = (int(self.center_w), 0)
        c2 = (int(self.width), int(self.height*0.25))
        c3 = (int(self.width), int(self.height*0.75))
        c4 = (int(self.center_w), int(self.height))
        c5 = (0, int(self.height*0.75))
        c6 = (0, int(self.height*0.25))
        return (c1, c2, c3, c4, c5, c6)
