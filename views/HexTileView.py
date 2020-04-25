from pygame.sprite import Sprite
from pygame import (
    Surface,
    init,
    display,
    draw,
    SRCALPHA
)

class HexTileView(Sprite):
    def __init__(self, size, cube, data):
        super().__init__()
        self.width, self.height = size*0.5*(3**0.5), size
        self.center_w, self.center_h = self.width*0.5, self.height*0.5

        self.cube = cube
        self.data = data
        self.image = Surface((self.width, self.height), SRCALPHA)
        self.rect = None 
        self.position = self.calculate_position()
        self.draw_hexagon()

    def draw_hexagon(self):
        hexagon_corners = self.calculate_corners()
        self.rect = draw.polygon(self.image, (0,0,0), hexagon_corners)

    def calculate_position(self):
        x = self.cube.offset_x
        y = self.cube.offset_y
        if y % 2:
            pos = (self.width*x + self.width*0.5, self.height*0.75*y)
        else:
            pos = (self.width*x, self.height*0.75*y)
        return pos

    def calculate_corners(self):

        c1 = (self.center_w, 0)
        c2 = (self.width, self.height*0.25) 
        c3 = (self.width, self.height*0.75)
        c4 = (self.center_w, self.height)
        c5 = (0, self.height*0.75)
        c6 = (0, self.height*0.25)
        return (c1, c2, c3, c4, c5, c6)
