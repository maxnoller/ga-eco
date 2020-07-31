import pygame

class Interface:
    def __init__(self, position, dimension, world, creature_manager, display):
        self.rect = Rect(position[0], position[1], dimension[0], dimension[1])
        self.world = world
        self.creature_manager = creature_manager
        self.display = display
    
    def draw_interface(self):
        pygame.draw.rect(self.display,
                         (255, 255, 255),
                         self.rect)