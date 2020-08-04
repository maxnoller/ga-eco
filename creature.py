import numpy as np
import random

from dna import DNA
from gui.helper_functions import GuiHelperFunctions
from brain.creature_brain import Brain
from observer import Observable, Event

class Creature(Observable):
    def __init__(self, max_health, hunger_damage, hunger, world):
        super().__init__()
        #hunger damage per second
        self.health = max_health
        self.hunger_damage = hunger_damage
        self.hunger = hunger
        self.current_food = 100
        self.position = (300, 300)
        self.rotation = 90
        self.world = world
        self.brain = Brain(self)
        self.speed_modifier = 0.7
        self.reproduce_cooldown = 10
        self.death = Event()
        self.reproduce = Event()

    def get_color(self):
        color_value = (self.health/100)*255
        return (color_value, color_value/2, color_value/2)

    def walk(self, speed):
        walk_cords = GuiHelperFunctions.pol2cart(speed*self.speed_modifier, self.rotation)
        if(self.world.can_move((self.position[0] + walk_cords[0], self.position[1] + walk_cords[1]))):
            self.position = (self.position[0] + walk_cords[0], self.position[1] + walk_cords[1])
            self.current_food -= speed * self.speed_modifier * 1.5
    
    def eat(self):
        if self.world.try_eat(self.position):
            self.current_food += 10
            if(self.current_food > 100):
                self.current_food = 100

    def update(self, delta_time):
        self.execute_brain()
        if self.current_food <= 0:
            self.current_food = 0
            self.change_health(-self.hunger_damage * (delta_time/1000))
            return
        self.current_food -= self.hunger * (delta_time/1000)
        self.reproduce_cooldown -= (delta_time/1000)
        self.try_reproduce()

    def try_reproduce(self):
        if self.reproduce_cooldown <= 0 and self.current_food >= 50:
            self.current_food -= 50
            self.reproduce.call(self)
            self.reproduce_cooldown = 10

    def change_health(self, amount):
        self.health += amount
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
                                                self.current_food,
                                                self.health)
        self.rotation = brain_output[1]*180/3.1415 # output from rad to degree
        self.walk(brain_output[0])
        if(brain_output[2] > 0.4):
            self.eat()
        if(brain_output[3] > 0.4):
            self.try_reproduce()
