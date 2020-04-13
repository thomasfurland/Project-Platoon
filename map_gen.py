import random

def random_map(width, height):
    result = []
    for _ in range(height):
        row = [random.randrange(3) for _ in range(width)]
        result.append(row)
    return result

def print_map(map):
    for i in map:
        print(i)

print_map(random_map(6, 4))