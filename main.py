from window import Window
from event_handler import EventHandler
from game_loop import GameLoop


fps = 2
window = Window((960, 540), (0, 0, 0))
event_handler = EventHandler(window)

for frame in GameLoop(window, fps):
    frame.beginning()

    event_handler.probe()

    frame.end()