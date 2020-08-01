import inspect

from tiles.world_tile import WorldTile
from tiles.border_tile import BorderTile
from tiles.water_tile import WaterTile
from tiles.food_tile import FoodTile


class World:
    def __init__(self, width, height, nrof_tiles):
        self.tile_size = height//nrof_tiles
        self.world = []
        self.width = nrof_tiles
        self.height = nrof_tiles
        self.create_tiles()

    def update(self, delta_time):
        for x in self.world:
            for tile in x:
                tile.update(delta_time)
    
    def create_tiles(self):
        for x in range(self.width):
            y_list = []
            for y in range(self.height):
                tile = FoodTile(100, 10)
                if x == (self.width-1) or x == 0 or y == 0 or y == (self.height-1):
                    tile = BorderTile()
                y_list.append(tile)
            self.world.append(y_list)

    def get_tile(self, position):
        x = int(position[0]//self.tile_size)
        y = int(position[1]//self.tile_size)
        if(x < 0 or x > self.width-1 or y < 0 or y > self.height-1):
            return BorderTile()
        return self.world[x][y]

    def try_eat(self, position):
        current_tile = self.get_tile(position)
        if isinstance(current_tile, FoodTile):
            return current_tile.eat()
        return False

    def can_move(self, position):
        return not isinstance(self.get_tile(position), BorderTile)

    def __str__(self):
        return_string = """World {} x {} tile size: {} \n""".format(self.width,
                                                                self.height,
                                                                self.tile_size)
        for col in self.world:
            line_str = [str(element) + " " for element in col]
            return_string = return_string + ("".join(line_str)+"\n")
        return return_string