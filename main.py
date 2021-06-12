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
    clock = pygame.time.Clock()

    done = False

    gm.load()

    # Main Game Loop
    while not done:

        event = pygame.event.Event(pygame.USEREVENT)

        # close the app
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        gm.update()
        gm.draw()
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
