

class Map:
    def __init__(self, shortest):
        self._shortest = shortest
        self.map_array = []

    def generate(self):
        for i in range(self._shortest):
            self.map_array.append(f"land{self._shortest}")
        print(self.map_array)

map = Map(3)
map.generate()
