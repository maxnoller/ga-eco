import pygame
import cProfile

from gui.gui import Gui
from creature import Creature
from world import World
from creature_manager import CreatureManager

def main_loop():
    done = False
    creatures.create_creatures(100)

    last_time = 0
    while not done:
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(clock.get_fps())
                    done = True

        current_ticks = pygame.time.get_ticks()
        delta_time = current_ticks - last_time
        last_time = current_ticks

        update_creatures(delta_time)

        gui.draw()

        pygame.display.flip()

def update_creatures(delta_time):
    for creature in creatures.creatures:
        creature.update(delta_time)

if __name__ == "__main__":
    pygame.init()
    world = World(600, 600, 100)
    creatures = CreatureManager(world)
    clock = pygame.time.Clock()
    gui = Gui(1000, 600, creatures, world, clock)
    cProfile.run("main_loop()")

