from player import Player


class Game:
    # game constructor
    def __init__(self, screen):
        self.screen = screen
        # array of all the map objects
        self.mapObjects = []

    # load class method
    def load(self):
        player = Player()
        self.mapObjects.append(player)

    # update class method
    def update(self):
        pass

    # draw class method
    def draw(self):
        pass
