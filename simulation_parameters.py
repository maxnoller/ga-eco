class SimulationParameters:
    def __init__(self, fps=30, world_pixel_size=(600,600), world_nrof_tiles=100, nrof_creatures=50):
        self.options = {"fps": fps,
                        "world_pixel_size": world_pixel_size,
                        "world_nrof_tiles": world_nrof_tiles,
                        "nrof_creatures": nrof_creatures
                        }