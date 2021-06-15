import pygame

import config
from draw_area import DrawArea
from player import Player
from game_map import GameMap
from direction import Directions as dir
from animation import ScreenAnimationManager


class Game:

    # game constructor
    def __init__(self, screen) -> None:
        self.screen = screen
        # create the area that gonna be drawn
        self.draw_area = DrawArea(0, 0, config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        # dictionary containing all the gameMap
        self.animation_manager = ScreenAnimationManager()
        self.maps = {}
        self.maps['FirstMap'] = GameMap(160, 144, "non.png", "interieur_test_collision.txt", self.animation_manager)
        self.maps['SecondMap'] = GameMap(800, 320, "route_2.png", "route_2.txt", self.animation_manager)
        self.currentMap = self.maps['SecondMap']

        self.player = Player(self.draw_area, self.currentMap)
        self.current_state = config.GAME_STATE_EXPLORATION

        self.load()

    # load class method
    def load(self) -> None:
        self.currentMap.load_map()
        self.currentMap.map_objects.append(self.player)

    # update class method
    def update(self) -> None:
        if self.current_state == config.GAME_STATE_EXPLORATION:
            self.handle_event()
            for map_objects in self.currentMap.map_objects:
                map_objects.update()
            if self.animation_manager.have_animation():
                if self.animation_manager.get_current_animation().isFinished:
                    self.animation_manager.pop_current_animation()


    # draw class method
    def draw(self) -> None:
        surface_to_draw = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        # the player move in the world
        if self.current_state == config.GAME_STATE_EXPLORATION:
            # fill the screen black
            self.screen.fill((0, 0, 0))
            self.currentMap.draw(surface_to_draw, self.draw_area)
            for map_object in self.currentMap.map_objects:
                map_object.draw(surface_to_draw)

        elif self.current_state == config.GAME_STATE_BATTLE:
            pass

        if self.animation_manager.have_animation():
            self.animation_manager.get_current_animation().update(surface_to_draw)

        self.screen.blit(surface_to_draw, (0, 0))




        self.screen.blit(surface_to_draw, (0, 0))

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
