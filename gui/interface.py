import pygame
import pygame.freetype

class Interface:
    """The interface class draws an interfaced used to retreive debug
       information and control the simulation"""
    def __init__(self, position, dimension, world, creature_manager, clock, display):
        self.rect = pygame.Rect(position[0], position[1], dimension[0], dimension[1])
        self.world = world
        self.creature_manager = creature_manager
        self.display = display
        self.font = pygame.freetype.SysFont("Calibri", 24)
        self.clock = clock

    def draw_interface(self):
        """Draws the whole interface on the display"""
        pygame.draw.rect(self.display,
                         (255, 255, 255),
                         self.rect)
        self.draw_fps()

    def draw_fps(self):
        """Draw a fps counter obtained from pygame onto the interface"""
        position = (self.rect.topright[0]-40, self.rect.topright[1])
        self.font.render_to(self.display, position, str(int(self.clock.get_fps())))

    def draw_creature_details(self, creature):
        """Displays details for the creature currently selected"""
        return
