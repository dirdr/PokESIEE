import pygame
import draw_area
import pokemon
import trainer


class Battle:

    def __init__(self, player: trainer.Trainer, opponent: trainer.Trainer) -> None:
        self.player_pokemon = pokemon.Pokemon
        self.opponent_pokemon = pokemon.Pokemon
        self.player_trainer = player
        self.opponent_trainer = trainer

    def begin(self, screen, area):
        self.starting_battle_animation(screen, area)
        pass

    def process_one_turn(self):
        pass

    def choose_new_pokemon(self):
        pass

    def attempt_to_run_away(self):
        pass

    def play_player_turn(self):
        pass

    def starting_battle_animation(self, screen: pygame.Surface, area: draw_area.DrawArea):
        pass

