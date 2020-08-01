import pygame
import cProfile

from gui.gui import Gui
from creature import Creature
from world import World
from creature_manager import CreatureManager

def main_loop():
    done = False
    creature_manager.create_creatures(100)

    last_time = 0
    currently_selected = None
    while not done:
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(clock.get_fps())
                    done = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    currently_selected = gui.check_mouse_click(pos[0], pos[1])

        current_ticks = pygame.time.get_ticks()
        delta_time = current_ticks - last_time
        last_time = current_ticks

        creature_manager.update_creatures(delta_time)
        world.update(delta_time)

        gui.draw(currently_selected)

        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    world = World(600, 600, 100)
    creature_manager = CreatureManager(world)
    clock = pygame.time.Clock()
    gui = Gui(1000, 600, creature_manager, world, clock)
    cProfile.run("main_loop()")

