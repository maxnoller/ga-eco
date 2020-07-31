import pygame
import cProfile

from gui import Gui
from creature import Creature
from world import World

creatures = []
def main_loop():
    done = False
    for i in range(100):
        creatures.append(Creature(100, 10, 1, world))

    last_time = 0;

    while not done:
        clock.tick(30)
        print(clock.get_fps())
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

        current_ticks = pygame.time.get_ticks()
        delta_time = current_ticks - last_time
        last_time = current_ticks

        update_creatures(delta_time)

        gui.draw_world()
        gui.draw_creatures()

        pygame.display.flip()

def update_creatures(delta_time):
    for creature in creatures:
        creature.update(delta_time)

if __name__ == "__main__":
    pygame.init()
    world = World(800, 800, 100)
    gui = Gui(800, 800, creatures, world)
    clock = pygame.time.Clock()
    cProfile.run("main_loop()")

