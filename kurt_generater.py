from Cube import Cube

class MapController:
    def __init__(self, generater):
        self.generater = generater

    def generate(self):
        self.generater.generate()


class RingGenerater:
    def __init__(self, rings:int):
        self.rings = rings

    def generate(self):
        pass


if __name__ == '__main__':
    xgen = RingGenerater(3)
    xmap = MapController(xgen)
    xmap.generate()