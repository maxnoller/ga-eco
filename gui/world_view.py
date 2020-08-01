import pygame

class WorldView:
    def __init__(self, world, screen):
        self.world = world
        self.screen = screen

    def draw_world(self):
        pygame.draw.rect(self.screen,
                         (0, 255, 0),
                         pygame.Rect(0, 0, self.world.tile_size*self.world.width, self.world.tile_size*self.world.height))
        for x in range(0, self.world.width):
            for y in range(0, self.world.height):
                if(self.world.world[x][y].get_color() != (0, 255, 0)):
                    self.draw_tile(x, y)

    def draw_tile(self, x, y):
        pygame.draw.rect(self.screen,
                         self.world.world[x][y].get_color(),
                         pygame.Rect(x*self.world.tile_size,
                                     y*self.world.tile_size,
                                     self.world.tile_size,
                                     self.world.tile_size)
                         )