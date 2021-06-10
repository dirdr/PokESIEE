import pygame

from player import Player
from entity import Entity


class Game:

    # game constructor
    def __init__(self, screen):
        self.screen = screen
        # array of all the map objects
        self.mapObjects = []
        self.background = Entity(636, 641, "fond_temp.png")

    # load class method
    def load(self) -> None:
        player = Player(300, 200)
        self.mapObjects.append(player)

    # update class method
    def update(self) -> None:
        for map_objects in self.mapObjects:
            map_objects.update()

    # draw class method
    def draw(self) -> None:
        self.screen.blit(pygame.transform.scale(self.background.image, (500, 500)) , (0, 0))
        for map_objects in self.mapObjects:
            map_objects.draw(self.screen)
