import pygame

from .helper_functions import GuiHelperFunctions

class CreatureView:
    """This class offers the functionality to draw creatures on to the simulation display"""
    def __init__(self, creature_manager, screen, creature_size):
        self.creature_manager = creature_manager
        self.creature_size = creature_size
        self.screen = screen

    def draw_creatures(self):
        """Draw all the creatures currently registered to the creature manager
           onto the screen according to their attributes"""
        for creature in self.creature_manager.get_creatures():
            points = [(0, self.creature_size/2),
                      (-self.creature_size/2, -self.creature_size/2),
                      (+self.creature_size/2, -self.creature_size/2)]
            coordinates = GuiHelperFunctions.convert_creature_cords(points, creature.rotation)
            pygame.draw.polygon(self.screen,
                                creature.get_color(),
                                GuiHelperFunctions.convert_rel_to_abs_cords(coordinates,
                                                                            creature.position))
