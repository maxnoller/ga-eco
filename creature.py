import numpy as np
import random

from dna import DNA
from gui.helper_functions import GuiHelperFunctions
from brain.creature_brain import Brain
from observer import Observable, Event

class Creature(Observable):
    def __init__(self, position, dna, creature_information, world):
        super().__init__()
        self.information = creature_information
        self.dna = dna
        self.current_food = dna.max_food
        self.health = dna.max_health
        self.reproduce_cooldown = dna.reproduce_cooldown
        self.position = position
        self.rotation = 90
        self.world = world
        self.brain = Brain(self)
        self.death = Event()
        self.reproduce = Event()
        self.close_creatures = 0

    def get_color(self):
        return self.dna.color

    def walk(self, speed):
        walk_cords = GuiHelperFunctions.pol2cart(speed*self.dna.speed_modifier, self.rotation)
        if(self.world.can_move((self.position[0] + walk_cords[0], self.position[1] + walk_cords[1]))):
            self.position = (self.position[0] + walk_cords[0], self.position[1] + walk_cords[1])
        self.change_food(-speed * self.dna.speed_modifier * 2)
    
    def eat(self):
        if self.world.try_eat(self.position):
            self.change_food(10)

    def update(self, delta_time):
        self.execute_brain()
        #self.current_food -= self.dna.hunger * (delta_time/1000)
        self.regenerate()
        self.hunger_damage(delta_time)
        self.reproduce_cooldown -= (delta_time/1000)
        self.try_reproduce()

    def hunger_damage(self, delta_time):
        if self.current_food <= 0:
            self.current_food = 0
            self.change_health(-self.dna.hunger_damage * (delta_time/1000))
    
    def regenerate(self):
        if self.current_food >= 90:
            self.change_health(10)
            self.change_food(-10)

    def try_reproduce(self):
        if self.reproduce_cooldown <= 0 and self.current_food >= 75:
            self.current_food -= 50
            self.health -= 25
            self.reproduce.call(self)
            self.reproduce_cooldown = self.dna.reproduce_cooldown

    def change_food(self, amount):
        self.current_food += amount
        if self.current_food > 100:
            self.current_food = 100

    def change_health(self, amount):
        self.health += amount
        if(self.health > 100):
            self.health = 100
        if(self.health <= 0):
            self.death.call(self)

    def get_current_tile(self):
        return self.world.get_tile(self.position[0], self.position[1])

    def see(self):
        tiles = []
        tiles.append(self.world.get_tile(self.position).get_color())
        polPos = GuiHelperFunctions.cart2pol(self.position[0], self.position[1])
        tiles.append(self.world.get_tile
                    (GuiHelperFunctions.pol2cart(polPos[0]+self.world.tile_size,
                                                 polPos[1])).get_color())
        tiles.append(self.world.get_tile
            (GuiHelperFunctions.pol2cart(polPos[0]+self.world.tile_size,
                                            polPos[1]-45)).get_color())
        tiles.append(self.world.get_tile
                    (GuiHelperFunctions.pol2cart(polPos[0]+self.world.tile_size,
                                                 polPos[1]+45)).get_color())
        return tiles

    def execute_brain(self):
        brain_output = self.brain.process_input(self.see(),
                                                self.close_creatures,
                                                self.current_food,
                                                self.health)
        self.rotation = np.rad2deg(brain_output[1]*2*3.1415)
        self.walk(brain_output[0])
        if(brain_output[2] > 0.4):
            self.eat()
        if(brain_output[3] > 0.4):
            self.try_reproduce()