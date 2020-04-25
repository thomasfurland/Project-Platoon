class Cube:
    def __init__(self, x, y, z):
        if x + y + z != 0:
            raise ValueError("x + y + z needs to equal 0")
        self.x = x
        self.y = y
        self.z = z
        #even-row offset
        self.offset_x, self.offset_y = self.cube_to_offset(x, z) 

    def __hash__(self):
        return hash(f"{self.x}_{self.y}_{self.z}")

    def __eq__(self, other):
        if isinstance(other, Cube):
            return hash(self) == hash(other)
        return False

    def __str__(self):
        return f'{self.x},{self.y},{self.z}'

    def __repr__(self):
        return f"<Cube {self.x} {self.y} {self.z}>"

    @classmethod
    def from_string(cls, x_y_z):
        x, y, z = x_y_z.split('_')
        return cls(int(x), int(y), int(z))

    def cube_to_offset(self, x, z):
        offset_x = x + (z + (abs(z) % 2))/ 2
        offset_y = z
        return int(offset_x), int(offset_y)

if __name__ == '__main__':
    x = {
        Cube(1, 2, -3): 'object1',
        Cube(1, 3, -4): 'object2'
    }
    print(x[Cube(1, 2, -3)]) # => 'object1'
    cube = Cube(0,0,0)
    print(cube.offset_x, cube.offset_y)
