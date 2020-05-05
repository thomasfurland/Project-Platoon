from pygame import KEYDOWN, K_e, K_t
from controls.events.event_controller import Event
from controls.Generate import GenerateMap
from models.Hexmap import HexMap

class NewEvanMap(Event):
    type_ = KEYDOWN

    def __call__(self, **kwargs):
        if kwargs["key"] == K_n:
            gamemap = HexMap()
            gamemap.map = GenerateMap("Evan")


class NewThomasMap(Event):
    type_ = KEYDOWN

    def __call__(self, **kwargs):
        if kwargs["key"] == K_n:
            gamemap = HexMap()
            gamemap.map = GenerateMap("Thomas")


            
