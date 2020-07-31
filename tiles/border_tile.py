from .world_tile import WorldTile

class BorderTile(WorldTile):
    def __init__(self):
        pass

    def get_color(self):
        return (0, 0, 0)
    
    def __str__(self):
        return "BT"