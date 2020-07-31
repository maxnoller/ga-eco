from creature import Creature

class CreatureManager:
    def __init__(self, world):
        self.world = world
        self.creatures = []

    def create_creatures(self, nrof_creatures):
        for i in range(nrof_creatures):
           self.create_creature()

    def create_creature(self):
        creature = Creature(100, 10, 1, self.world, self.handle_death)
        self.creatures.append(creature)

    def handle_death(self, creature):
        self.creatures.remove(creature)