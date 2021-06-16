import pygame
import pokemon
import trainer
import os
import config
import animation
import trainer


class Battle:

    def __init__(self, animation_manager: animation.ScreenAnimationManager, player: trainer.Trainer) -> None:

        self.anim_manager = animation_manager
        self.image_path = "ui/pokemon_battle_background.png"
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(config.image, self.image_path)),
                                            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.loaded = False
        self.player = player

    def has_been_loaded(self) -> bool:
        return self.loaded


    def process_one_turn(self) -> None:
        pass

    def choose_new_pokemon(self) -> None:
        pass

    def attempt_to_run_away(self) -> None:
        pass

    def play_player_turn(self) -> None:
        pass

    def update(self) -> None:
        pass


# this class is a child class of a general Battle, it represent a battle between the player and a Trainer with multiple pokemon
class TrainerBattle(Battle):

    def __init__(self, animation_manager: animation.ScreenAnimationManager, player: trainer.Trainer, opponent: trainer.Trainer) -> None:
        super(TrainerBattle, self).__init__(animation_manager, player)
        self.opponent = opponent
        self.opponent_pokemon_sprite = opponent.get_current_pokemon().front_image
        self.player_pokemon_sprite = player.get_current_pokemon().front_image

    def draw(self, surface) -> None:
        surface.blit(self.image, (0, 0))


# this class is a child class of a general Battle, it represent a battle between the player and a wild pokemon
class WildBattle(Battle):

    def __init__(self, animation_manager: animation.ScreenAnimationManager, player: trainer.Trainer, wild_pokemon: pokemon.Pokemon) -> None:
        super(WildBattle, self).__init__(animation_manager, player)
        self.wild_pokemon = wild_pokemon
        self.opponent_sprite = wild_pokemon.front_image
        self.player_pokemon_sprite = player.get_current_pokemon().front_image
        self.need_to_draw_wild_pokemon = True
        self.need_to_draw_player_pokemon = True

        print("le combat que vous venez de commencer va voir s'affronter :")
        print(self.player.get_current_pokemon().get_name())
        print("contre")
        print(self.wild_pokemon.get_name())

    def draw(self, surface) -> None:
        surface.blit(self.image, (0, 0))
        self.draw_opponent_pokemon(surface)
        self.draw_player_pokemon(surface)
        print(self.anim_manager.animation_queue)

    def draw_opponent_pokemon(self, surface) -> None:
        self.need_to_draw_wild_pokemon = True
        for anim in self.anim_manager.animation_queue:
            if isinstance(anim, animation.OpponentEnterBattle):
                self.need_to_draw_wild_pokemon = False
        if self.need_to_draw_wild_pokemon:
            surface.blit(self.wild_pokemon.front_image, (325, 40))

    def draw_player_pokemon(self, surface) -> None:
        self.need_to_draw_player_pokemon = True
        for anim in self.anim_manager.animation_queue:
            if isinstance(anim, animation.PlayerPokemonEnterBattle):
                self.need_to_draw_player_pokemon = False
        if self.need_to_draw_player_pokemon:
            print("debug")
            surface.blit(self.player.get_current_pokemon().back_image, (60, 144))

    # play the starting animation
    def begin(self) -> None:
        self.anim_manager.add_animation(animation.RectAnimation())
        self.anim_manager.add_animation(animation.TextDisplay("Un " + self.wild_pokemon.get_name() + " sauvage apparait!"))
        self.anim_manager.add_animation(animation.OpponentEnterBattle(self.wild_pokemon))
        self.anim_manager.add_animation(animation.PlayerEnterBattle())
        self.anim_manager.add_animation(animation.TextDisplay("en Avant " + self.player.get_current_pokemon().get_name() + " !"))
        self.anim_manager.add_animation(animation.PlayerPokemonEnterBattle(self.player.get_current_pokemon()))
        self.loaded = True
