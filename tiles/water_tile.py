from .world_tile import WorldTile

class WaterTile(WorldTile):
    def __init__(self):
        self.color = (0, 0, 255)

    def get_color(self):
        return (0, 0, 255)

