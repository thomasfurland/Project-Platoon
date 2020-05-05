from window import Window
from controls.EventHandler import EventHandler
#from controls.Renderer import Renderer
from game_loop import GameLoop
from models.HexMap import HexMap
fps = 2
window = Window((960, 540), (0, 0, 0))
event_handler = EventHandler(window)
#renderer = Renderer(window)

for frame in GameLoop(window, fps):
    frame.beginning()

    event_handler.probe()
    #renderer.render_visuals()
    Map = HexMap()
    print(len(Map.map))
    frame.end()
