from .creature import Creature

class CreatureManager:
    def __init__(self, width, height):
        self.dimensions = (width, height)
        self.creatures = []

    def create_creatures(self, nrof_creatures, random_positions=True):
        for i in range(nrof_creatures):
            if random_

    def create_creature(self, position):
        self.creatures += Creature()