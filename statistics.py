from observer import Observer

class Statistics():
    def __init__(self, creature_manager):
        self.population_statistics = PopulationStatistics(creature_manager)

class PopulationStatistics(Observer):
    def __init__(self, creature_manager):
        self.creature_manager = creature_manager
        self.population_history = []
        creature_manager.attach(self)

    def __del__(self):
        self.creature_manager.detach(self)

    def update(self, observable):
        self.population_history.append(len(observable.get_creatures()))

    def __str__(self):
        return str(self.population_history[-1])