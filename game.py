import pygame
import config
import pokemon
import trainer
from draw_area import DrawArea
from player import Player
from game_map import GameMap
from direction import Directions as dir
from animation import ScreenAnimationManager
from gsm import GameStateManager
from pokemon import Pokemon


class Game:

    # game constructor
    def __init__(self, screen) -> None:
        # load all pokemon in the game
        Pokemon.load_pokemons()
        # red variable
        self.screen = screen
        # create the area that gonna be drawn
        self.draw_area = DrawArea(0, 0, config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        # dictionary containing all the gameMap
        self.animation_manager = ScreenAnimationManager()
        self.gsm = GameStateManager(config.GAME_STATE_EXPLORATION)
        self.maps = {}
        self.player_trainer = trainer.Trainer(pokemon.get_poke(17))
        self.pokemon_list = {}
        self.load_pokemon_list_in_map()
        self.load_map()
        self.currentMap = self.maps['Route2']
        self.player = Player(self.draw_area, self.currentMap)
        self.load()

    def load_map(self):
        self.maps['Route2'] = GameMap(800, 320, "map_image/route_2.png", "route_2.txt", self.animation_manager,
                                      self.gsm,
                                      self.pokemon_list['Route2'], self.player_trainer)

    def load_pokemon_list_in_map(self):

        self.pokemon_list['Route1'] = [
            pokemon.get_poke(16),
            pokemon.get_poke(19),
            pokemon.get_poke(25),
            pokemon.get_poke(261),
        ]
        self.pokemon_list['Route2'] = [
            pokemon.get_poke(58),
            pokemon.get_poke(43),
            pokemon.get_poke(231),
            pokemon.get_poke(29),
            pokemon.get_poke(32),
            pokemon.get_poke(403),
            pokemon.get_poke(276),
            pokemon.get_poke(532)
        ]
        self.pokemon_list['ForetMaudite'] = [
            pokemon.get_poke(92),
            pokemon.get_poke(200),
            pokemon.get_poke(406),
            pokemon.get_poke(543),
            pokemon.get_poke(355),
            pokemon.get_poke(198),
            pokemon.get_poke(451),
        ]
        self.pokemon_list['Manoir'] = [
            pokemon.get_poke(92),
            pokemon.get_poke(355),
            pokemon.get_poke(200),
            pokemon.get_poke(442),
            pokemon.get_poke(228),
            pokemon.get_poke(607),
        ]
        self.pokemon_list['Route3'] = [
            pokemon.get_poke(246),
            pokemon.get_poke(309),
            pokemon.get_poke(624),
            pokemon.get_poke(626),
            pokemon.get_poke(396),
            pokemon.get_poke(287),
            pokemon.get_poke(179)
        ]
        self.pokemon_list['DesertDelassant'] = [
            pokemon.get_poke(27),
            pokemon.get_poke(111),
            pokemon.get_poke(304),
            pokemon.get_poke(529),
            pokemon.get_poke(551)
        ]

        self.pokemon_list['Route4'] = [
            pokemon.get_poke(322),
            pokemon.get_poke(449),
            pokemon.get_poke(115),
            pokemon.get_poke(344),
        ]

        self.pokemon_list['Route5'] = [
            pokemon.get_poke(350),
            pokemon.get_poke(437),
            pokemon.get_poke(589),
            pokemon.get_poke(617)
        ]

        self.pokemon_list['Grotte'] = [
            pokemon.get_poke(614),
            pokemon.get_poke(473),
            pokemon.get_poke(362),
            pokemon.get_poke(76),
            pokemon.get_poke(472)
        ]

        self.pokemon_list['Route6'] = [
            pokemon.get_poke(350),
            pokemon.get_poke(437),
            pokemon.get_poke(589),
            pokemon.get_poke(617)
        ]

    # load class method
    def load(self) -> None:
        self.currentMap.load_map()
        self.currentMap.map_objects.append(self.player)

    # update class method
    def update(self) -> None:

        self.handle_event()

        if self.gsm.get_current_state() == config.GAME_STATE_EXPLORATION:
            for map_objects in self.currentMap.map_objects:
                map_objects.update()

        elif self.gsm.get_current_state() == config.GAME_STATE_BATTLE:
            if not self.gsm.current_battle.has_been_loaded():
                self.gsm.current_battle.begin()
            self.gsm.current_battle.update()

        if self.animation_manager.have_animation():
            if self.animation_manager.get_current_animation().isFinished:
                self.animation_manager.pop_current_animation()
        else:
            self.gsm.update_state()

    # draw class method
    def draw(self) -> None:

        self.screen.fill((0, 0, 0))

        surface_to_draw = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        if not self.animation_manager.have_animation():
            self.gsm.update_state()

        if self.gsm.get_current_state() == config.GAME_STATE_EXPLORATION:
            # fill the screen black
            self.currentMap.draw(surface_to_draw, self.draw_area)
            for map_object in self.currentMap.map_objects:
                map_object.draw(surface_to_draw)

        elif self.gsm.get_current_state() == config.GAME_STATE_BATTLE:
            if self.gsm.current_battle.has_been_loaded():
                self.gsm.current_battle.draw(surface_to_draw)

        if self.animation_manager.have_animation():
            current_anim = self.animation_manager.get_current_animation()
            current_anim.update(surface_to_draw)

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


