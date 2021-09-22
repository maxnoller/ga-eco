from typing import Tuple

from .world_tile import WorldTile

class BorderTile(WorldTile):
    """WorldTile which is supposed to sit on the border of the world"""
    def __init__(self):
        pass

    def get_color(self) -> Tuple[int,int,int]:
        return (255, 0, 0)
    
    def __str__(self) -> str:
        return "BT"