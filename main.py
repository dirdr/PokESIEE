import pygame
import config
from game import Game
pygame.init()

# screen
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("PokESIEE")


# create a new instance of game
gm = Game(screen)
clock = pygame.time.Clock()

done = False

# Main Game Loop
while not done:

    event = pygame.event.Event(pygame.USEREVENT)

    # close the app
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    gm.update()
    clock.tick(30)
    pygame.display.flip()


pygame.quit()
