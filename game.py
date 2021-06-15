import pygame

import config
from draw_area import DrawArea
from player import Player
from entity import Entity
from game_map import GameMap
from direction import Directions as dir


class Game:

    # game constructor
    def __init__(self, screen) -> None:
        self.screen = screen
        # create the area that gonna be drawn
        self.draw_area = DrawArea(-50, -10, config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        # dictionary containing all the gameMap
        self.maps = {}
        self.maps['FirstMap'] = GameMap(160, 144, "non.png", "interieur_test_collision.txt")
        self.maps['SecondMap'] = GameMap(800, 320, "route_2.png", "route_2.txt")
        self.currentMap = self.maps['FirstMap']
        self.player = Player(self.draw_area, self.currentMap)
        self.load()

    # load class method
    def load(self) -> None:
        self.currentMap.load_map()
        self.currentMap.map_objects.append(self.player)

    # update class method
    def update(self) -> None:
        self.handle_event()
        for map_objects in self.currentMap.map_objects:
            map_objects.update()

    # draw class method
    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.currentMap.draw(self.screen, self.draw_area)
        for map_object in self.currentMap.map_objects:
            map_object.draw(self.screen)

    def handle_event(self) -> None:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.MAIN_LOOP_DOWN = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_n and self.player.current_mode == config.PLAYER_MODE_WALK:
                    self.player.next_mode = config.PLAYER_MODE_RUN

                if event.key == pygame.K_DOWN:
                    self.player.directionPressed[dir.SOUTH] = True
                if event.key == pygame.K_UP:
                    self.player.directionPressed[dir.NORTH] = True
                if event.key == pygame.K_LEFT:
                    self.player.directionPressed[dir.WEST] = True
                if event.key == pygame.K_RIGHT:
                    self.player.directionPressed[dir.EAST] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_n and self.player.current_mode == config.PLAYER_MODE_RUN:
                    self.player.next_mode = config.PLAYER_MODE_WALK
                if event.key == pygame.K_DOWN:
                    self.player.release_direction(dir.SOUTH)
                if event.key == pygame.K_UP:
                    self.player.release_direction(dir.NORTH)
                if event.key == pygame.K_LEFT:
                    self.player.release_direction(dir.WEST)
                if event.key == pygame.K_RIGHT:
                    self.player.release_direction(dir.EAST)
