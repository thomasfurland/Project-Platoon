from time import time as time_now
from pygame import quit as pygame_quit


class GameLoop:
    def __init__(self, window, fps):
        self.window = window
        self.delay = 1/fps
    
    def __iter__(self):
        self.last = time_now()
        return self

    def __next__(self):
        while self.window.running:
            curr = time_now()
            if curr - self.last >= self.delay:
                self.last = curr
                return self.window.frame
        pygame_quit()
        raise StopIteration()
