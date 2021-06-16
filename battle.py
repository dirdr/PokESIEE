import pygame
import draw_area
import pokemon
import trainer
import os
import config
import animation
import text_display


class Battle:

    def __init__(self, animation_manager: animation.ScreenAnimationManager, type_of_battle: int) -> None:
        self.type_of_battle = type_of_battle
        self.anim_manager = animation_manager
        self.player_pokemon = pokemon.Pokemon
        self.opponent_pokemon = pokemon.Pokemon
        self.player_trainer = trainer.Trainer
        self.opponent_trainer = trainer
        self.image_path = "pokemon_battle_background.png"
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(config.assets, self.image_path)),
                                            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.loaded = False
        self.text_util_display = text_display.TextDisplay()

    def has_been_loaded(self):
        return self.loaded

    # play the starting animation
    def begin(self):
        self.anim_manager.add_animation(animation.RectAnimation())
        self.anim_manager.add_animation(animation.PlayerEnterBattle())
        self.loaded = True

    def process_one_turn(self):
        pass

    def choose_new_pokemon(self):
        pass

    def attempt_to_run_away(self):
        pass

    def play_player_turn(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
        self.text_util_display.box_display_text("un pokemon sauvage viens d'apparaitre", surface)

    def update(self):
        pass
