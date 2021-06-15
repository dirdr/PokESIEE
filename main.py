import pygame
import config
from game import Game
pygame.init()

if __name__ == '__main__':

    # screen
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("PokESIEE")

    # create a new instance of game
    gm = Game(screen)

    done = False

    gm.load()

    # Main Game Loop
    while not config.MAIN_LOOP_DOWN:
        gm.update()
        gm.draw()
        config.GAME_CLOCK.tick(60)
        pygame.display.flip()

    pygame.quit()
