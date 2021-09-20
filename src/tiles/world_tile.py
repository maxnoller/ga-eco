from abc import ABC, abstractmethod

class WorldTile(ABC):
    """WorldTile base class for representing part of a tile based world"""

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def update(self, delta_time):
        pass