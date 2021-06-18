import pygame
import localisation
import warp
from battle import Battle
import config
import pokemon
import trainer
from draw_area import DrawArea
from player import Player
from game_map import GameMap
from direction import Directions as dir
from animation import ScreenAnimationManager
from pokemon import Pokemon
from ability import loadmoves


class Game:

    # game constructor
    def __init__(self, screen) -> None:
        # load all pokemon in the game
        Pokemon.load_pokemons()
        # red variable
        self.screen = screen
        # create the area that gonna be drawn
        self.draw_area = DrawArea(0, 0, config.SCREEN_WIDTH, config.SCREEN_HEIGHT)

        player_premier_pokemon = pokemon.get_poke(306)
        player_premier_pokemon.learn(loadmoves.ALL_MOVES["charge"])
        self.player_trainer = trainer.Trainer(player_premier_pokemon)

        self.animation_manager = ScreenAnimationManager()
        # dictionary containing all the gameMap
        self.maps = {}
        self.load_map()
        self.localisation_list = {}
        self.localisations_objet = localisation.Localisations(self)
        self.current_localisation = self.localisation_list['Route2']
        self.next_localisation = localisation.Localisation({}, {}, "test")
        self.current_state = config.GAME_STATE_EXPLORATION
        self.next_state = config.GAME_STATE_EXPLORATION
        self.current_battle = Battle
        self.player = Player(self.draw_area, self)
        self.current_localisation.map.map_objects.append(self.player)
        self.option = ''


    def load_map(self):

        pokemon_list = {'Route1': [
            pokemon.get_poke(16),
            pokemon.get_poke(19),
            pokemon.get_poke(25),
            pokemon.get_poke(261),
        ], 'Route2': [
            pokemon.get_poke(58),
            pokemon.get_poke(43),
            pokemon.get_poke(231),
            pokemon.get_poke(29),
            pokemon.get_poke(32),
            pokemon.get_poke(403),
            pokemon.get_poke(276),
            pokemon.get_poke(532)
        ], 'ForetMaudite': [
            pokemon.get_poke(92),
            pokemon.get_poke(200),
            pokemon.get_poke(406),
            pokemon.get_poke(543),
            pokemon.get_poke(355),
            pokemon.get_poke(198),
            pokemon.get_poke(451),
        ], 'Manoir': [
            pokemon.get_poke(92),
            pokemon.get_poke(355),
            pokemon.get_poke(200),
            pokemon.get_poke(442),
            pokemon.get_poke(228),
            pokemon.get_poke(607),
        ], 'Route3': [
            pokemon.get_poke(246),
            pokemon.get_poke(309),
            pokemon.get_poke(624),
            pokemon.get_poke(626),
            pokemon.get_poke(396),
            pokemon.get_poke(287),
            pokemon.get_poke(179)
        ], 'DesertDelassant': [
            pokemon.get_poke(27),
            pokemon.get_poke(111),
            pokemon.get_poke(304),
            pokemon.get_poke(529),
            pokemon.get_poke(551)
        ], 'Route4': [
            pokemon.get_poke(322),
            pokemon.get_poke(449),
            pokemon.get_poke(115),
            pokemon.get_poke(344),
        ], 'Route5': [
            pokemon.get_poke(350),
            pokemon.get_poke(437),
            pokemon.get_poke(589),
            pokemon.get_poke(617)
        ], 'Grotte': [
            pokemon.get_poke(614),
            pokemon.get_poke(473),
            pokemon.get_poke(362),
            pokemon.get_poke(76),
            pokemon.get_poke(472)
        ], 'Route6': [
            pokemon.get_poke(350),
            pokemon.get_poke(437),
            pokemon.get_poke(589),
            pokemon.get_poke(617)
        ]}

        self.maps['Route2'] = GameMap(801, 321, "map_image/route_2.png", "route_2.txt",
                                      pokemon_list['Route2'], "Route2", self)

        print(pokemon_list['Route2'])

        self.maps['Route2'].load_map_array()

        self.maps['ForetMaudite'] = GameMap(768, 704, "map_image/Foret.png", "Foret.txt",
                                            pokemon_list['ForetMaudite'], 'ForetMaudite', self)

        self.maps['ForetMaudite'].load_map_array()

        self.maps['Ville1'] = GameMap(640, 640, "map_image/Ville_1.png", "Ville_1.txt", [], 'Ville1', self)
        self.maps['Ville1'].load_map_array()



    # update class method
    def update(self) -> None:

        self.handle_event()
        if self.current_state == config.GAME_STATE_EXPLORATION:
            for map_objects in self.current_localisation.map.map_objects:
                map_objects.update()

        elif self.current_state == config.GAME_STATE_BATTLE:
            if not self.current_battle.has_been_loaded():
                self.current_battle.begin()
            else:
                self.current_battle.update()

        if self.animation_manager.have_animation():
            if self.animation_manager.get_current_animation().isFinished:
                self.animation_manager.pop_current_animation()
                self.update_state()
        else:
            self.update_state()

    # update the current map to the next map
    def update_map(self):
        self.current_localisation = self.next_localisation

    # update the current state to the next state
    def update_state(self):
        self.current_state = self.next_state

    # request a game state change
    def request_state_change(self, state):
        self.next_state = state

    # draw class method
    def draw(self) -> None:

        self.screen.fill((0, 0, 0))
        surface_to_draw = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        if self.current_state == config.GAME_STATE_EXPLORATION:
            # fill the screen black
            self.current_localisation.map.draw(surface_to_draw, self.draw_area)
            for map_object in self.current_localisation.map.map_objects:
                map_object.draw(surface_to_draw)

        elif self.current_state == config.GAME_STATE_BATTLE:
            if self.current_battle.has_been_loaded():
                self.current_battle.draw(surface_to_draw)

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

    def new_battle(self, battle):
        self.current_battle = battle

    def load_next_localisation(self):
        inverse_option = warp.find_opposite(self.option)
        new_player_coordinate = self.next_localisation.warp[inverse_option]
        self.player.change_current_tile(new_player_coordinate)
        self.player.update_coordinates()
        self.next_localisation.map.map_objects.append(self.player)
        self.player.game_map = self.next_localisation.map
        self.next_localisation.map.load_map_array()
        self.update_map()
        pygame.time.wait(100)

    def change_next_localisation(self):
        self.next_localisation = self.current_localisation.get_exit(self.option)
