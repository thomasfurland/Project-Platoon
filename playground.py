from Cube import Cube
from HexMap import HexMap
from evan_generate import MapGen
from evan_front_end import frontEnd

H = 5
W = 7

genner = MapGen()
genner.generator(H,W)
game_board = HexMap(genner.map)

front = frontEnd(H,W,5)
for cube in game_board.map.keys():
    front.add_hextile(cube)

i=1
for tile_xrow in front.tile_arr:
    print('\nRow',i)
    for tile in tile_xrow:
        print(tile)
    i += 1