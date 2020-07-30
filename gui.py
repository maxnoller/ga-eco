import pygame
import math
import numpy as np

from world import World

class Gui:
    def __init__(self, width, height, creatures, world):
        self.tile_size = world.tile_size
        self.done = False
        self.world = world
        self.screen = pygame.display.set_mode((width, height))
        self.creatures = creatures
        
    def draw_creatures(self):
        for creature in self.creatures:
            points = [(0, self.tile_size/2),
                      (-self.tile_size/2, -self.tile_size/2),
                      (+self.tile_size/2, -self.tile_size/2)]
            coordinates = Gui.convert_creature_cords(points, creature.rotation)
            pygame.draw.polygon(self.screen,
                                (255,255,255),
                                Gui.convert_rel_to_abs_cords(coordinates, creature.position))

    @staticmethod
    def convert_rel_to_abs_cords(relative_coordinates, center_point):
        return_coordinates = []
        for (x,y) in relative_coordinates:
            return_coordinates.append((center_point[0]+x, center_point[1]+y))
        return return_coordinates

    @staticmethod
    def convert_creature_cords(coordinates, alpha):
        return_coordinates = []
        for (x,y) in coordinates:
            (rho, phi) = Gui.cart2pol(x,y)
            return_coordinates.append(Gui.pol2cart(rho,phi+np.deg2rad(alpha)))
        return return_coordinates

    @staticmethod
    def cart2pol(x, y):
        rho = np.sqrt(x**2 + y**2)
        phi = np.arctan2(y, x)
        return(rho, phi)

    @staticmethod
    def pol2cart(rho, phi):
        x = rho * np.cos(phi)
        y = rho * np.sin(phi)
        return(x, y)

    def draw_world(self):
        pygame.draw.rect(self.screen,
                         (0, 255, 0),
                         pygame.Rect(0, 0, self.world.tile_size*self.world.width, self.world.tile_size*self.world.height))
        for x in range(self.world.width):
            for y in range(self.world.height):
                if(self.world.world[x][y].get_color() != (0, 255, 0)):
                    self.draw_tile(x, y)

    def draw_tile(self, x, y):
        pygame.draw.rect(self.screen,
                         self.world.world[x][y].get_color(),
                         pygame.Rect(x*self.world.tile_size,
                                     y*self.world.tile_size,
                                     (x+1)*self.world.tile_size-1,
                                     (y+1)*self.world.tile_size-1)
                         )