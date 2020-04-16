class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __hash__(self):
        return hash(f"{self.x}_{self.y}_{self.z}")

    def __eq__(self, other):
        if isinstance(other, Cube):
            return hash(self) == hash(other)
        return False

    @classmethod
    def from_string(cls, x_y_z):
        x, y, z = x_y_z.split('_')
        return cls(int(x), int(y), int(z))

    

if __name__ == '__main__':
    x = {
        Cube(1, 2, 3): 'object1',
        Cube(1, 2, 4): 'object2'
    }
    print(x[Cube(1, 2, 3)]) # => 'object1'