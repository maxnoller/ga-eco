import pygame
import pygame.freetype
import inspect
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from creature import Creature

class Interface:
    """The interface class draws an interfaced used to retreive debug
       information and control the simulation"""
    def __init__(self, position, dimension, world, statistics, clock, display, speed):
        self.rect = pygame.Rect(position[0], position[1], dimension[0], dimension[1])
        self.world = world
        self.statistics = statistics
        self.display = display
        self.font = pygame.freetype.SysFont("Calibri", 24)
        self.clock = clock
        self.selected = None
        self.speed = speed
    
    def set_selected(self, element):
        if element is not None and self.selected is not element:
            self.selected = element

    def draw_interface(self):
        """Draws the whole interface on the display"""
        pygame.draw.rect(self.display,
                         (255, 255, 255),
                         self.rect)
        if isinstance(self.selected, Creature):
            self.draw_creature_details(self.selected)
        
        self.draw_fps()
        self.draw_nrof_creatures()

    def draw_fps(self):
        """Draw a fps counter obtained from pygame onto the interface"""
        position = (self.rect.topright[0]-40, self.rect.topright[1]+10)
        self.fps_rect = self.font.render_to(self.display, position, str(int(self.clock.get_fps())))
        #if self.fps_rect.collidepoint(pygame.mouse.get_pos()):
        #    print("hit")
        #    self.font.render_to(self.display, pygame.mouse.get_pos(), "FPS")

    def draw_nrof_creatures(self):
        position = (self.rect.topright[0]-40, self.rect.topright[1]+40)
        self.font.render_to(self.display, position, str(self.statistics.population_statistics))

    def draw_creature_details(self, creature):
        """Displays details for the creature currently selected"""
        position_title = (self.rect.topleft[0]+10, self.rect.topleft[1]+10)
        position_food = (self.rect.topleft[0]+10, self.rect.topleft[1]+30)
        position_health = (self.rect.topleft[0]+10, self.rect.topleft[1]+50)
        position_generation = (self.rect.topleft[0]+10, self.rect.topleft[1]+70)
        position_close_creatures = (self.rect.topleft[0]+10, self.rect.topleft[1]+90)
        self.font.render_to(self.display, position_title, "Creature")
        self.font.render_to(self.display, position_food, "Food: "+str(int(creature.current_food))+"/100")
        self.font.render_to(self.display, position_health, "Health: "+str(int(creature.health))+"/100")
        self.font.render_to(self.display, position_generation, "Generation: "+str(creature.information.generation))
        self.font.render_to(self.display, position_close_creatures, "Close creatures:"+str(creature.close_creatures))
        #self.draw_creature_vision(creature)
        return

    

    def check_click(self, x, y):
        if self.fps_rect.collidepoint(x, y):
            return 

    def setup_time(self):
        self.slider = Slider(self.display, self.rect.bottomleft[0]-100, self.rect.bottomleft[1]-100, 100, 20, min=0, max=5, step=0.1)
        self.slider.setValue(self.speed)
        self.output = TextBox(self.display, 475, 200, 50, 50, fontSize=30)
        self.output.disable()

    def update_time(self):
        self.output.setText(self.slider.getValue())
        self.speed = self.slider.getValue()