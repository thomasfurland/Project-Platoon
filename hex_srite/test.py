from pygame.sprite import Sprite
from pygame import (
    Surface,
    init,
    display, 
    draw,
    time, 
    event,
    key,
    QUIT, 
    K_UP, 
    K_DOWN
)

class Tile(Sprite):
    def __init__(self, display_surface, color, x, y, size):
        super().__init__()
        width = size
        height = size

        height_q = height // 4
        width_q = width // 4

        self.image = Surface((width, height))

        self.rect = draw.polygon(self.image, color, (
            (0, height_q), (width_q*2, 0), (width, height_q),
            (width, height_q*3), (width_q*2, height), (0, height_q*3)
        ))

        if y % 2:
            pos = ((width * x) + (width_q * 2), (height_q * 3) * y)
        else:
            pos = ((width * x), (height_q * 3) * y)
        display_surface.blit(self.image, pos)


if __name__ == '__main__':
    init()

    width = 960
    height = 540

    center = (width//2, height//2)
    window_surface = display.set_mode((width, height))
    display.set_caption("Center Main")

    size = 50

    run = True
    while run:
        time.delay(50)

        for i in event.get():
            if i.type == QUIT:
                run = False

        keys = key.get_pressed()
        if keys[K_UP]:
            size += (size // 10)
        if keys[K_DOWN]:
            size -= (size // 10)


        window_surface.fill((0, 0, 0))

        Tile(window_surface, (173, 216, 230), 0, 0, size)
        Tile(window_surface, (0, 128, 255), 1, 0, size)
        Tile(window_surface, (173, 216, 230), 2, 0, size)

        Tile(window_surface, (255,127,80), 0, 1, size)
        Tile(window_surface, (255,69,0), 1, 1, size)
        Tile(window_surface, (255,127,80), 2, 1, size)

        Tile(window_surface, (173, 216, 230), 0, 2, size)
        Tile(window_surface, (0, 128, 255), 1, 2, size)
        Tile(window_surface, (173, 216, 230), 2, 2, size)

        Tile(window_surface, (255,127,80), 0, 3, size)
        Tile(window_surface, (255,69,0), 1, 3, size)
        Tile(window_surface, (255,127,80), 2, 3, size)

        display.update()