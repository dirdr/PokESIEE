from entity import Entity
from player import Player
from entity import Entity


class Game:
    # game constructor
    def __init__(self, screen):
        self.screen = screen
        # array of all the map objects
        self.mapObjects = []
        self.bakground = Entity()

    # load class method
    def load(self):
        player = Player()
        self.mapObjects.append(player)

    # update class method
    def update(self):
        self.bakground.update()
        for map_objects in self.mapObjects:
            map_objects.update()

    # draw class method
    def draw(self):
        self.bakground.draw(self.screeen)
        for map_objects in self.mapObjects:
            map_objects.draw(self.screen)
