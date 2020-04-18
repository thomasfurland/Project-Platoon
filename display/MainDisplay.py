import pygame
from pygame.locals import *

class MainDisplay:
    def __init__(self, width, height):
        pygame.init()
        self.size = width, height
        self.display = pygame.display.set_mode(self.size)
        self.background = pygame.Surface(self.display.get_size()).convert() 

    def run(self):
        while True:
            for event in pygame.event.get():
                self.handle_event(event)
            self.render_objects()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    def render_objects(self):
        self.display.blit(self.background, (0,0))
        pygame.display.flip()

    def set_bg_colour(self, r, g, b):
       self.background.fill((r, g, b))

    def set_title(self, title):
        pygame.display.set_caption(title)

if __name__ == '__main__':
    GAME = MainDisplay(640, 480)
    GAME.set_title("Map Gen Testing")
    GAME.set_bg_colour(250, 250, 250) #white
    GAME.run()
