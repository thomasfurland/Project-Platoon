

class Map:
    def __init__(self, shortest):
        self._shortest = shortest
        self.map_array = []

    def generate(self):
        print(self._shortest)

map = Map(3)
map.generate()