import inspect
import numpy as np
import noise

from tiles.world_tile import WorldTile
from tiles.border_tile import BorderTile
from tiles.water_tile import WaterTile
from tiles.food_tile import FoodTile


class World:
    def __init__(self, position, nrof_tiles):
        self.tile_size = position[1]//nrof_tiles
        self.world = []
        self.width = nrof_tiles
        self.height = nrof_tiles
        self.noise_to_tiles()

    def update(self, delta_time):
        for x in self.world:
            for tile in x:
                tile.update(delta_time)

    def noise_to_tiles(self):
        noise = self.noisemap()
        self.world = []
        for x in range(self.width):
            y_list = []
            for y in range(self.height):
                if x == (self.width-1) or x == 0 or y == 0 or y == (self.height-1):
                    y_list.append(BorderTile())
                elif noise[x][y] < -0.05:
                   y_list.append(WaterTile())
                else:
                    y_list.append(FoodTile(100, 5))
            self.world.append(y_list)


    def noisemap(self, scale=25, octaves=2, persistence=0.5, lacunarity=2.0):
        shape = (self.width, self.height)
        seed = np.random.randint(0,100)
        world_noise = np.zeros(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                world_noise[i][j] = noise.pnoise2(i/scale,
                                                  j/scale,
                                                  octaves=octaves,
                                                  persistence=persistence,
                                                  lacunarity=lacunarity,
                                                  repeatx=1024,
                                                  repeaty=1024,
                                                  base=seed)
        return world_noise

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