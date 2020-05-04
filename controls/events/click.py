from pygame import MOUSEBUTTONDOWN, draw
from controls.events.event_controller import Event

import random

def random_color():
    return (
        random.randint(0, 255)
        ,random.randint(0, 255)
        ,random.randint(0, 255)
    )

class ChangeLeft(Event):
    type_ = MOUSEBUTTONDOWN

    def __call__(self, **kwargs):
        window = self._controller.window
        if kwargs['pos'][0] <= window._surface.get_rect().centerx:
            draw.rect(window._surface, random_color(), (0, 0, 480, 540))
        

class ChangeRight(Event):
    type_ = MOUSEBUTTONDOWN

    def __call__(self, **kwargs):
        window = self._controller.window
        if kwargs['pos'][0] > window._surface.get_rect().centerx:
            draw.rect(window._surface, random_color(), (480, 0, 480, 540))
