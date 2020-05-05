from pygame import KEYDOWN, K_e, K_t
from controls.events.event_controller import Event
from controls.datagen import MapFactory

class NewEvanMap(Event):
    type_ = KEYDOWN

    def __call__(self, **kwargs):
        if kwargs["key"] == K_e:
            hexmap = MapFactory()("Evan")
            hexmap.generate(11,15)

class NewThomasMap(Event):
    type_ = KEYDOWN

    def __call__(self, **kwargs):
        if kwargs["key"] == K_t:
            hexmap = MapFactory()("Thomas")
            hexmap.generate(7,7)
            
