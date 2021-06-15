import os
import config
import game
from entity import Entity
import pygame
import random
import animation


def debug_draw_grid(screen):

    x_temp = 0
    y_temp = 0
    for i in range(0, 16):
        pygame.draw.line(screen, (0, 0, 0), (x_temp, y_temp), (x_temp, config.SCREEN_HEIGHT), 1)
        x_temp += 32

    x_temp = 0
    y_temp = 0
    for i in range(0, 11):
        pygame.draw.line(screen, (0, 0, 0),  (x_temp, y_temp), (config.SCREEN_WIDTH, y_temp), 1)
        y_temp += 32


class GameMap(Entity):

    # game_map constructor
    def __init__(self, width: int, height: int, image_path: str, collision_path: str, animation_manager):
        super(GameMap, self).__init__(width, height, image_path)
        self.animation_manager = animation_manager
        self.tile_size = config.TILE_SIZE_SCALED
        self.number_of_tiles_width = int(2*self.width/self.tile_size)
        self.number_of_tiles_height = int(2*self.height/self.tile_size)
        self.map_objects = []
        self.map_grid = []
        self.character_list = []
        self.collision_path = collision_path

    # draw the game_map
    def draw(self, screen, draw_area) -> None:
        screen.blit(self.scaled, (0, 0), area=draw_area.update_rect())

    # Load the map file into the field map_grid
    def load_map(self) -> None:
        with open(os.path.join(config.map_assets, self.collision_path)) as f:
            line_array = f.read().splitlines()
            f.close()
        for line in line_array:
            line_array = []
            for char in line:
                line_array.append(char)
            self.map_grid.append(line_array)

    def handle_grass_event(self):
        random_number = random.random()
        if random_number < config.FIND_POKEMON_CHANCE_BOUND:
            # if we find a pokemon, add a new animation to the queue
            self.animation_manager.animation_queue.append(animation.ScreenFade(10))

            # create a new pokemon found in the map pokemon list
            # TODO
            print("vous venez de tomber sur un pokemon sauvage")

































