import pygame
import cProfile
import time
import argparse

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
        clock.tick(fps)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    gui.mouse_click(pos[0], pos[1])
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        highest_gen = creature_manager.get_creature_highest_generation()
                        gui.interface.set_selected(highest_gen)
                        gui.creature_view.marked_creature = highest_gen

        current_ticks = pygame.time.get_ticks()
        delta_time = speed*(current_ticks - last_time) 
        last_time = current_ticks

        creature_manager.update_creatures(delta_time)
        world.update(delta_time)

        gui.draw()

        pygame.display.update()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--speed", type=float, help="simulation speed, default = 1", default=1)
    parser.add_argument("--fps", help="frames per second, default=30", type=int, default=30)
    args = parser.parse_args()
    pygame.init()
    speed = args.speed
    fps = args.fps
    parameters = SimulationParameters()
    world = World(parameters.options["world_pixel_size"], parameters.options["world_nrof_tiles"])
    creature_manager = CreatureManager(parameters.options["nrof_creatures"], world)
    statistics = Statistics(creature_manager)
    clock = pygame.time.Clock()
    gui = Gui(1000, 600, creature_manager, world, clock, statistics, speed)
    main_loop()
    #cProfile.run("main_loop()")

"""
TODO: Implement Pause function
TODO: Implement Neural Network Viewer
TODO: Partial Screen udpates
TODO: Collect all variables/constants and make them be changeable by parameter or a file
TODO: Creature vision viewer
TODO: Something about the borders
"""