import random
import math
from numba import jit
from pprint import pprint

from creature import Creature
from brain.creature_brain import Brain
from observer import Observable
from dna import DNA
from quadtree import QuadTree
from creature_information import CreatureInformation

class CreatureManager(Observable):
    def __init__(self, nrof_creatures, world):
        super().__init__()
        self.nrof_creatures = nrof_creatures
        self.world = world
        self.creatures = QuadTree(600, 600)

    def create_creatures(self, nrof_creatures):
        """create nrof_creatures creatures"""
        for i in range(nrof_creatures):
           self.create_creature()

    def create_creature(self, position=None, creature_information=CreatureInformation(0, None)):
        """create a creature with default parameters"""
        if(position is None): position = (int(random.uniform(0, 400)), int(random.uniform(0, 400)))
        information = creature_information
        dna = DNA(100, 100, 1, 5)
        #print(f"x:{position[0]} y:{position[1]}")
        creature = Creature(position, dna, information, self.world)
        self.register(creature, position)
        return creature

    def register(self, creature, position):
        self.creatures.insert(creature, position[0], position[1])
        creature.reproduce.register(self.create_offspring)
        creature.death.register(self.handle_death)
        self.notify()

    def unregister(self, creature):
        creature.reproduce.unregister(self.create_offspring)
        creature.death.unregister(self.handle_death)
        self.creatures.remove(creature)

    def handle_death(self, creature):
        """handle the death of a creature by unregistering it"""
        try:
            self.unregister(creature)
            self.notify()
        except ValueError as e:
            print("Tried removing unregistered creature from creature_manager")

    def get_creatures(self):
        """get all currently registered creatures"""
        return self.creatures.all()

    def update_creatures(self, delta_time):
        if(len(self.get_creatures()) < self.nrof_creatures):
            self.create_creatures(1)
        for creature in self.get_creatures():
            self.get_close_creatures(creature)
            creature.update(delta_time)

    def get_close_creatures(self, creature):
        creature.close_creatures = len(self.creatures.get_neighbors(creature.position[0], creature.position[1], creature.dna.sense_distance))

    def get_creature_highest_generation(self):
        return sorted(self.get_creatures(), key=lambda creature : creature.information.generation)[-1]

    def create_offspring(self, creature):
        creature_information = CreatureInformation(creature.information.generation+1, creature)
        new_position = (creature.position[0]+5, creature.position[1]+5)
        offspring = self.create_creature(position=creature.position, creature_information=creature_information)
        offspring.brain = Brain.from_existing_brain(creature.brain)
        offspring.brain.mutate()