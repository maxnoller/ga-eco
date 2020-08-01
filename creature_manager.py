from creature import Creature

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
        creature = Creature(100, 10, 10, self.world, self.handle_death)
        self.creatures.append(creature)

    def handle_death(self, creature):
        """handle the death of a creature by unregistering it"""
        self.creatures.remove(creature)

    def get_creatures(self):
        """get all currently registered creatures"""
        return self.creatures

    def update_creatures(self, delta_time):
        for creature in self.creatures:
            creature.update(delta_time)