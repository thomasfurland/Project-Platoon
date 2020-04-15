class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        if isinstance(other, Cube):
            return hash(self) == hash(other)
        return False

    @classmethod
    def from_string(cls, x_y_z):
        x, y, z = x_y_z.split('_')
        return cls(int(x), int(y), int(z))