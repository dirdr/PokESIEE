import animation
import pygame
import config
import os


class BattleUpdater:

    def __init__(self, battle):
        self.battle = battle
        self.image_path = "ui/pokemon_battle_background.png"
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(config.image, self.image_path)),
                                            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.user_input = ''
        self.current_state = config.BATTLE_STATE_WAIT_FOR_USER_INPUT
        self.next_state = config.BATTLE_STATE_WAIT_FOR_USER_INPUT
        self.queue = self.battle.queue
        self.anim_manager = self.battle.anim_manager
        self.need_to_draw_wild_pokemon = False
        self.need_to_draw_player_pokemon = False

    def update(self):
        if not self.anim_manager.have_animation():
            print(self.queue.event_queue)
            if self.queue.have_event():
                self.queue.get_current_event().update()
            if self.queue.have_event() and self.queue.get_current_event().isFinished:
                self.current_state = config.BATTLE_STATE_READY_TO_PROGRESS
                self.user_input = self.queue.get_current_event().get_user_input()
                self.queue.pop_current_event()

        self.check_first_user_input()

    def check_first_user_input(self):
        if self.current_state == config.BATTLE_STATE_READY_TO_PROGRESS:
            if self.user_input == "Attaque":
                self.battle.play_turn()
            if self.user_input == "Fuite":
                print("vous essayez de prendre la fuite")
            if self.user_input == "Pokémon":
                print('vous essayez de changer de pokemon')
            if self.user_input == 'Capture':
                print("vous essayez de capturer")

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
        self.draw_opponent_pokemon(surface)
        self.draw_player_pokemon(surface)
        if not self.anim_manager.have_animation():
            if self.queue.have_event():
                self.queue.get_current_event().draw(surface)

    def change_state(self):
        self.current_state = self.next_state

    def request_new_state(self, state):
        self.next_state = state

    def draw_opponent_pokemon(self, surface) -> None:
        self.need_to_draw_wild_pokemon = True
        for anim in self.anim_manager.animation_queue:
            if isinstance(anim, animation.OpponentEnterBattle):
                self.need_to_draw_wild_pokemon = False
        if self.need_to_draw_wild_pokemon:
            surface.blit(self.battle.wild_pokemon.front_image, (325, 40))

    def draw_player_pokemon(self, surface) -> None:
        self.need_to_draw_player_pokemon = True
        for anim in self.anim_manager.animation_queue:
            if isinstance(anim, animation.PlayerPokemonEnterBattle):
                self.need_to_draw_player_pokemon = False
        if self.need_to_draw_player_pokemon:
            surface.blit(self.battle.player.get_current_pokemon().back_image, (60, 135))