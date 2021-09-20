import pygame

from .helper_functions import GuiHelperFunctions

class CreatureView:
    """This class offers the functionality to draw creatures on to the simulation display"""
    def __init__(self, creature_manager, screen, creature_size):
        self.creature_manager = creature_manager
        self.creature_size = creature_size
        self.screen = screen
        self.marked_creature = None

    def draw_creatures(self):
        """Draw all the creatures currently registered to the creature manager
           onto the screen according to their attributes"""
        self.creature_rects = []
        for creature in self.creature_manager.get_creatures():
            color = creature.get_color()
            if self.marked_creature is not None and creature is self.marked_creature.information.parent:
                color = (255, 0, 0)
            points = [(0, self.creature_size/2),
                      (-self.creature_size/2, -self.creature_size/2),
                      (+self.creature_size/2, -self.creature_size/2)]
            coordinates = GuiHelperFunctions.convert_creature_cords(points, creature.rotation)
            rect = pygame.draw.polygon(self.screen,
                                color,
                                GuiHelperFunctions.convert_rel_to_abs_cords(coordinates,
                                                                            creature.position))
            self.creature_rects.append(rect)
            if(creature is self.marked_creature):
                pygame.draw.circle(self.screen,
                                   (255,0,0),
                                   CreatureView.convert_float_to_int_cords(creature.position),
                                   20,
                                   1)
    
    @staticmethod
    def convert_float_to_int_cords(position):
        return (int(position[0]), int(position[1]))

    def check_if_creature_clicked(self, x, y):
        for idx, rect in enumerate(self.creature_rects):
            if rect.collidepoint(x, y):
                self.mark_creature(self.creature_manager.get_creatures()[idx])
                return self.creature_manager.get_creatures()[idx]

    def mark_creature(self, creature):
        self.marked_creature = creature
    

