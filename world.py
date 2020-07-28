import inspect

from tiles.world_tile import WorldTile
from tiles.border_tile import BorderTile
from tiles.water_tile import WaterTile
from tiles.food_tile import FoodTile


class World:
    def __init__(self, width, height, nrof_tiles):
        self.tile_size = height/nrof_tiles
        self.world = []
        self.width = nrof_tiles
        self.height = nrof_tiles
        self.create_tiles()

        self.world[5][5] = WaterTile() #this just for testing 
    
    def create_tiles(self):
        for x in range(self.width):
            y_list = []
            for y in range(self.height):
                tile = FoodTile(x,y, 100)
                if x == (self.width-1) or x == 0 or y == 0 or y == (self.height-1):
                    tile = BorderTile()
                y_list.append(tile)
            self.world.append(y_list)

    def get_tile(self, position):
        x = position[0]//self.tile_size
        y = position[1]//self.tile_size
        return self.world[int(x)][int(y)]

    def try_eat(self, position):
        current_tile = self.get_tile(position)
        if isinstance(current_tile, FoodTile):
            current_tile.eat()
            return True
        return False

    def can_move(self, position):
        return not isinstance(self.get_tile(position), BorderTile)