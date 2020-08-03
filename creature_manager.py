from creature import Creature

from brain.creature_brain import Brain

class CreatureManager:
    def __init__(self, world):
        self.world = world
        self.creatures = []

    def create_creatures(self, nrof_creatures):
        """create nrof_creatures creatures"""
        for i in range(nrof_creatures):
           self.create_creature()

    def create_creature(self):
        """create a creature with default parameters"""
        creature = Creature(100, 10, 3, self.world, self.handle_death, self.create_offspring)
        self.register(creature)
        return creature

    def register(self, creature):
        self.creatures.append(creature)

    def handle_death(self, creature):
        """handle the death of a creature by unregistering it"""
        self.creatures.remove(creature)

    def get_creatures(self):
        """get all currently registered creatures"""
        return self.creatures

    def update_creatures(self, delta_time):
        if(len(self.creatures) < 40):
            self.create_creatures(40-(len(self.creatures)))
        for creature in self.creatures:
            creature.update(delta_time)

    def create_offspring(self, creature):
        print("child spawned")
        offspring = self.create_creature()
        offspring.brain = Brain.from_existing_brain(creature.brain)