import random

from creature import Creature
from brain.creature_brain import Brain
from observer import Observable
from dna import DNA
from creature_information import CreatureInformation

class CreatureManager(Observable):
    def __init__(self, world):
        super().__init__()
        self.world = world
        self.creatures = []

    def create_creatures(self, nrof_creatures):
        """create nrof_creatures creatures"""
        for i in range(nrof_creatures):
           self.create_creature()

    def create_creature(self, position=None, creature_information=CreatureInformation(0, None)):
        """create a creature with default parameters"""
        if(position is None): position = (random.uniform(0, 600), random.uniform(0, 600))
        information = creature_information
        dna = DNA(100, 100, 3, 10)
        creature = Creature(position, dna, information, self.world)
        self.register(creature)
        return creature

    def register(self, creature):
        self.creatures.append(creature)
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
        return self.creatures

    def update_creatures(self, delta_time):
        if(len(self.creatures) < 100):
            self.create_creatures(100-(len(self.creatures)))
        for creature in self.creatures:
            creature.update(delta_time)

    def create_offspring(self, creature):
        creature_information = CreatureInformation(creature.information.generation+1, creature)
        offspring = self.create_creature(position=creature.position, creature_information=creature_information)
        offspring.brain = Brain.from_existing_brain(creature.brain)
        offspring.brain.mutate()