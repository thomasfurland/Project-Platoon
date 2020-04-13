import random

def random_map(width, height):
    return [[
        random.randint(0, 3) for _ in range(width)
    ] for _ in range(height)]

print(random_map(6, 4))