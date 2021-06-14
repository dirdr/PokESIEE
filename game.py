import pygame

import config
from draw_area import DrawArea
from player import Player
from entity import Entity
from game_map import GameMap


class Game:

    # game constructor
    def __init__(self, screen) -> None:
        self.screen = screen
        # create the area that gonna be drawn
        self.draw_area = DrawArea(-50, -10, config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        # dictionary containing all the gameMap
        self.map = {'FirstMap': GameMap(160, 144, "interieur_test.png")}
        self.currentMap = self.map['FirstMap']
        self.load()

    # load class method
    def load(self) -> None:
        player = Player(self.draw_area, self.currentMap)
        self.map['FirstMap'].load_map()
        self.map['FirstMap'].map_objects.append(player)

    # update class method
    def update(self) -> None:
        for map_objects in self.currentMap.map_objects:
            map_objects.update()

    # draw class method
    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.currentMap.draw(self.screen, self.draw_area)
        for map_object in self.map['FirstMap'].map_objects:
            map_object.draw(self.screen)

    # take a map coordinate as a parameter and return the screen coordinate
    def convert_coordinate_map_to_screen(self, coordinate: tuple) -> tuple:
        returnable = (coordinate[0] - self.draw_area.x, coordinate[1] - self.draw_area.y)
        return returnable
