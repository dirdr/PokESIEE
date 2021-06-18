import os
import random

import pygame

import battle_event_queue
import selection_box
import animation
import config
import pokemon
import text_box
import trainer
from battle_updater import BattleUpdater


class Battle:

    def __init__(self, animation_manager: animation.ScreenAnimationManager, player: trainer.Trainer) -> None:
        self.anim_manager = animation_manager
        self.loaded = False
        self.player = player
        self.queue = battle_event_queue.BattleEventQueue()
        self.battle_updater = BattleUpdater(self)

    def has_been_loaded(self) -> bool:
        return self.loaded

    def begin(self) -> None:
        self.anim_manager.add_animation(animation.RectAnimation())

    def play_turn(self):
        self.queue.add_event(battle_event_queue.ChooseAttack(self.player.get_current_pokemon()))

    def process_one_turn(self) -> None:
        pass

    def choose_new_pokemon(self) -> None:
        pass

    def attempt_to_run_away(self) -> None:
        pass

    def update(self):
        self.battle_updater.update()

    def draw(self, surface):
        self.battle_updater.draw(surface)


# this class is a child class of a general Battle, it represent a battle between the player and a Trainer with multiple pokemon
class TrainerBattle(Battle):
    pass

# this class is a child class of a general Battle, it represent a battle between the player and a wild pokemon
class WildBattle(Battle):

    def __init__(self, animation_manager: animation.ScreenAnimationManager, player: trainer.Trainer,
                 wild_pokemon: pokemon.Pokemon) -> None:
        super(WildBattle, self).__init__(animation_manager, player)
        self.wild_pokemon = wild_pokemon
        self.opponent_sprite = wild_pokemon.front_image
        self.player_pokemon_sprite = player.get_current_pokemon().front_image

    # play the starting animation
    def begin(self) -> None:
        super().begin()
        self.anim_manager.add_animation(animation.OpponentEnterBattle(self.wild_pokemon))
        self.anim_manager.add_animation(animation.ListenableTextDisplay(["Un " + self.wild_pokemon.get_name() + " apparait ! ", ""]))
        self.anim_manager.add_animation(animation.ListenableTextDisplay(["En avant ", self.player.get_current_pokemon().get_name() + " !"]))
        self.anim_manager.add_animation(animation.PlayerEnterBattle())
        self.anim_manager.add_animation(animation.PlayerPokemonEnterBattle(self.player.get_current_pokemon()))
        # first user input
        self.queue.add_event(battle_event_queue.BattleEventOptionBoxAndTextBox(self.player))
        self.loaded = True

    def play_turn(self):
        super.play_turn()


class BattleMechanics:

    def __init(self):
        pass
    # return true if the player go first else False
    def goes_first(self, player: pokemon.Pokemon, opponent: pokemon.Pokemon) -> bool:
        if player.speed > opponent.speed:
            return True
        elif opponent.speed > player.speed:
            return False
        else:
            # same speed, speedTie
            return bool(random.getrandbits(1))

    def attempt_a_hit(self, move, user: pokemon.Pokemon, target: pokemon.Pokemon) -> bool:
        pass
