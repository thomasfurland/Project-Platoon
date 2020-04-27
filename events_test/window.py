from pygame import init as pygame_init, display


class Frame:
    def __init__(self, window):
        self.window = window
    
    def beginning(self):
        self.window.reset()

    def end(self):
        display.update()


class Window:
    def __init__(self, dimensions, bg_color):
        pygame_init()
        self.running = True
        self._surface = display.set_mode(dimensions)
        self._bg_color = bg_color
        self.frame = Frame(self)

    def reset(self):
        self._surface.fill(self._bg_color)

    def stop(self):
        self.running = False