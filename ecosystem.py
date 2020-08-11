import pygame
import cProfile
import time

from gui.gui import Gui
from creature import Creature
from world import World
from statistics import Statistics
from creature_manager import CreatureManager
from simulation_parameters import SimulationParameters

def main_loop():
    done = False

    last_time = 0
    start_time = time.time()
    nrof_frames = 0
    while not done:
        nrof_frames+=1
        clock.tick(30)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(nrof_frames/(time.time()-start_time))
                    done = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    gui.mouse_click(pos[0], pos[1])

        current_ticks = pygame.time.get_ticks()
        delta_time = (current_ticks - last_time) 
        last_time = current_ticks

        creature_manager.update_creatures(delta_time)
        world.update(delta_time)

        gui.draw()

        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    parameters = SimulationParameters()
    world = World(parameters.options["world_pixel_size"], parameters.options["world_nrof_tiles"])
    creature_manager = CreatureManager(parameters.options["nrof_creatures"], world)
    statistics = Statistics(creature_manager)
    clock = pygame.time.Clock()
    gui = Gui(1000, 600, creature_manager, world, clock, statistics)
    cProfile.run("main_loop()")

