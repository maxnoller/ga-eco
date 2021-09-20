from typing import Tuple
from .world_tile import WorldTile

class WaterTile(WorldTile):
    """WorldTile which represents water"""
    def __init__(self):
        self.color = (0, 0, 255)

    def get_color(self) -> Tuple[int,int,int]:
        return (0, 0, 255)

    def __str__(self) -> str:
        return "WT"