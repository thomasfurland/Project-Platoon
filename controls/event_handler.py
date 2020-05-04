from pygame import event, QUIT

from controls.events import EventController


class EventHandler:
    def __init__(self, window):
        self.window = window
        self.controller = EventController(window)

    def probe(self):
        for i in event.get():
            if i.type == QUIT:
                self.window.stop()
            else:
                self.controller.distribute(i)
