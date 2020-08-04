import pygame

from .interface import Interface
from .creature_view import CreatureView
from .world_view import WorldView

class Gui:
    def __init__(self, width, height, creatures, world, clock, statistics):
        self.screen = pygame.display.set_mode((width, height))
        self.interface = Interface((601, 0), (width-600, height), world, statistics, clock, self.screen)
        self.creature_view = CreatureView(creatures, self.screen, world.tile_size)
        self.world_view = WorldView(world, self.screen)

    def draw(self):
        self.interface.draw_interface()
        self.world_view.draw_world()
        self.creature_view.draw_creatures()

    def mouse_click(self, x, y):
        result = self.creature_view.check_if_creature_clicked(x, y)
        if result is not None:
            self.interface.set_selected(result)
        result = self.interface.check_click(x, y)
        if result is not None:
            self.interface.set_selected(result)
