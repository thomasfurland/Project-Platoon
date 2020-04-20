from Cube import Cube

class MapController:
    def __init__(self, generator):
        self.generator = generator
        self.hex_map = []

    def generate_map(self):
        self.hex_map = self.generator.generate()


class RingGenerator:
    def __init__(self, iterator, rings:int):
        self.iterator = iterator
        self.rings = rings

    def generate(self):
        result = [Cube(0, 0, 0)]
        for i in range(1, self.rings + 1):
            for x, y, z in self.iterator(i):
                result.append(Cube(x, y, z))
        return result


class RingIterator:
    def __init__(self, ring:int):
        self.ring = ring

    def __getitem__(self, key):
        if not isinstance(key, int):
            return getattr(self, key)
        keys = [self.x, self.y, self.z]
        return keys[key]
    
    def __setitem__(self, key, value):
        if not isinstance(key, int):
            setattr(self, key, value)
        else:
            keys = ['x', 'y', 'z']
            setattr(self, keys[key], value)

    def _current(self):
        return (self.x, self.y, self.z)

    def __iter__(self):
        self.x = -self.ring
        self.y = self.ring
        self.z = 0
        self.primary = 0 # 0 == x
        self.secondary = 2 # 2 == z
        return self

    def __next__(self):
        if self.primary < 6 and self.ring > 0:
            result = self._current()
            self[self.primary % 3] += 1
            self[self.secondary % 3] -= 1
            if self[self.primary % 3] == 0:
                self.secondary += 2
            if self[self.primary % 3] == self.ring:
                self.primary += 2
            return result
        raise StopIteration()


if __name__ == '__main__':
    xgen = RingGenerator(RingIterator, 1)
    xmap = MapController(xgen)
    xmap.generate_map()
    for cube in xmap.hex_map:
        print(repr(cube))