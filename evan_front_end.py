from Cube import Cube
from HexMap import HexMap

class frontEnd:
    def __init__(self,tile_height,tile_width,tile_size):
        self.tile_arr = [] #save tiles as list of lists. hextile accessed by tile_arr[x][y]
        self.tile_size = tile_size #this will be the radius r of the hextiles
        self.top_left_tile = Cube(-2,4,-2)   #once map is generated this value needs to be updated for pixel reference. Will be normally set to None before map is generated
        self._create_tile_arr(tile_height,tile_width) #add tiles to the list tile_arr

    def _create_tile_arr(self,height,width):    #makes sure the tile_arr has the proper dimension to be indexed and filled properly
        x_arr = [None for _ in range(width)]
        for _ in range(height):
            self.tile_arr.append(x_arr)

    def add_hextile(self,hextile):  #this method should run while the map is generated and HexTiles are created
        x = hextile.x
        y = hextile.y
        self.tile_arr[x][y] = hextile

    def hex2pix(self,hextile):  #this function, given a hextile, will return the pixel values (w,h) for that hextile's center
        w = (self.tile_size)*(3**0.5)*(0.5)*(hextile.x-self.top_left_tile.x-hextile.y+self.top_left_tile.y+1)
        h = (-self.tile_size)*(3/2)*(hextile.x-self.top_left_tile.x+hextile.y-self.top_left_tile.y-1)   #these are the stupidly complicated math formulas
        return (w,h)

    ###IDK HOW PIXELS WORK. ASSUMING THE w,h VALUES CAN BE ACCESSED VIA pixel.w AND pixel.h

    def pix2hex(self,pixel):    #this function, given a pixel, will return the 'close enough'values of the hextile's center
        x = pixel.w/(self.tile_size*(3**0.5)) -pixel.h/(3*self.tile_size) +self.top_left_tile.x
        y = -pixel.w/(self.tile_size*(3**0.5))-pixel.h/(3*self.tile_size) +self.top_left_tile.y +1
        return (int(x),int(y))
    
    def hextile_corners_pixel(self,center_pixel):    #given a pixel that is the center of a hextile, returns the pixel values of the 6 corners
        c1 = (center_pixel.w,center_pixel.h-self.tile_size)
        c2 = (center_pixel.w + self.tile_size*0.5*(3**0.5),center_pixel.h - self.tile_size*0.5)
        c3 = (center_pixel.w + self.tile_size*0.5*(3**0.5),center_pixel.h + self.tile_size*0.5)
        c4 = (center_pixel.w,center_pixel.h+self.tile_size)
        c5 = (center_pixel.w - self.tile_size*0.5*(3**0.5),center_pixel.h + self.tile_size*0.5)
        c6 = (center_pixel.w - self.tile_size*0.5*(3**0.5),center_pixel.h - self.tile_size*0.5)
        return(c1,c2,c3,c4,c5,c6)
