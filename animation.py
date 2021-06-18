from typing import Union

import pygame
import os
# this class contains many useful animation for battle etc
from pygame.surface import SurfaceType, Surface

import config
import pokemon
import spritesheet
import text_box


class ScreenAnimation:

    def __init__(self) -> None:
        self.isFinished = False
        self.alpha = 300

    def update(self, surface):
        pass


class ScreenFadeIn(ScreenAnimation):

    def __init__(self, speed: int) -> None:
        super(ScreenFadeIn, self).__init__()
        self.fade_speed = speed

    def update(self, surface) -> None:
        if self.alpha >= 0:
            surface.set_alpha(self.alpha)
            self.alpha -= self.fade_speed
        else:
            print("animation over")
            self.isFinished = True


class PlayerChooseAttack(ScreenAnimation):

    def __init__(self, poke: pokemon.Pokemon):
        super(PlayerChooseAttack, self).__init__()
        attack = poke.moves
        print(attack)


class ScreenFadeOut(ScreenAnimation):

    def __init__(self, speed: int) -> None:
        super(ScreenFadeOut, self).__init__()
        self.fade_speed = speed
        self.alpha = 0

    def update(self, surface) -> None:
        if self.alpha <= 300:
            surface.set_alpha(self.alpha)
            self.alpha += self.fade_speed
        else:
            self.isFinished = True


class BattleAnimation(ScreenAnimation):

    def __init__(self) -> None:
        super(BattleAnimation, self).__init__()
        self.fade_speed = 20
        self.rect_length_bottom = config.SCREEN_HEIGHT / 2
        self.rect_length_upper = config.SCREEN_HEIGHT / 2
        self.number_of_fade = 2
        self.timer = 0

    def update(self, surface: pygame.Surface) -> None:
        if self.alpha >= 0:
            surface.set_alpha(self.alpha)
            self.alpha -= self.fade_speed
        else:
            if self.number_of_fade >= 0:
                self.alpha = 300
                self.number_of_fade -= 1
            else:
                surface.set_alpha(0)
                self.isFinished = True


class RectAnimation(ScreenAnimation):

    def __init__(self) -> None:
        super(RectAnimation, self).__init__()
        self.timer = 0
        self.rect_length_bottom = config.SCREEN_HEIGHT / 2
        self.rect_length_upper = config.SCREEN_HEIGHT / 2

    def update(self, surface: pygame.Surface) -> None:
        bottom_rect = (0, self.rect_length_bottom, config.SCREEN_WIDTH, config.SCREEN_HEIGHT / 2)
        upper_rect = (0, 0, config.SCREEN_WIDTH, self.rect_length_upper)
        pygame.draw.rect(surface, (0, 0, 0), bottom_rect)
        pygame.draw.rect(surface, (0, 0, 0), upper_rect)
        if self.timer > 10:
            self.rect_length_bottom += 2
            self.rect_length_upper -= 2
        self.timer += 1

        if self.rect_length_upper < 0 and self.rect_length_bottom > config.SCREEN_HEIGHT:
            self.isFinished = True


class OpponentEnterBattle(ScreenAnimation):

    def __init__(self, opponent: pokemon.Pokemon) -> None:
        super(OpponentEnterBattle, self).__init__()
        self.opponent_sprite = opponent.front_image
        self.scaled = pygame.transform.scale2x(self.opponent_sprite)
        self.x = config.SCREEN_WIDTH + self.opponent_sprite.get_width()
        self.final_position_x = 325

    def update(self, surface) -> None:
        surface.blit(self.opponent_sprite, (self.x, 40))
        if self.x >= self.final_position_x:
            surface.blit(self.opponent_sprite, (self.x, 40))
            self.x -= 4
        else:
            self.isFinished = True


class PlayerPokemonEnterBattle(ScreenAnimation):

    def __init__(self, poke: pokemon.Pokemon):
        super(PlayerPokemonEnterBattle, self).__init__()
        self.pokemon_to_draw = poke
        self.need_to_show_pokemon = False
        self.fade = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.fade.fill((250, 255, 255))
        self.speed = 8

    def update(self, surface):
        if self.need_to_show_pokemon:
            surface.blit(self.pokemon_to_draw.back_image, (60, 144))
            self.isFinished = True
        else:
            if self.alpha >= 0:
                self.fade.set_alpha(self.alpha)
                self.alpha -= self.speed
                surface.blit(self.fade, (0, 0))
            else:
                self.need_to_show_pokemon = True


class PlayerEnterBattle(ScreenAnimation):

    def __init__(self) -> None:
        super(PlayerEnterBattle, self).__init__()
        self.player_sprite_sheet = pygame.image.load(os.path.join(config.image, "spritesheet/player_spritesheet.png"))
        self.sprites = []
        self.load_sprites()

        self.final_player_position_first_part = 80
        self.final_player_position_second_part = -20
        self.final_player_position_third_part = -40
        self.final_player_position_fourth_part = -120

        self.x_first_part = -50
        self.x_second_part = self.final_player_position_first_part
        self.x_third_part = self.final_player_position_second_part
        self.x_fourth_part = self.final_player_position_third_part

        self.y = 95
        self.pokeball_base_x = self.x_second_part + 8
        self.pokeball_base_y = 165
        self.pokeball_x = self.pokeball_base_x
        self.pokeball_y = self.pokeball_base_y

        self.need_to_show_pokeball = False

    def load_sprites(self) -> None:
        x_temp = 228

        for i in range(0, 4):
            sub_image = spritesheet.pick_image(self.player_sprite_sheet, x_temp, 0, 128, 128)
            self.sprites.append(sub_image)
            x_temp += 128
        self.sprites.append(
            pygame.transform.scale(pygame.image.load(os.path.join(config.image, "misc_sprite/poke_ball.png")),
                                   (20, 25)))

    def update(self, surface) -> None:

        # chain player movement
        if self.need_to_show_pokeball:
            surface.blit(self.sprites[4], (self.pokeball_x, self.pokeball_y))

        if self.x_first_part <= self.final_player_position_first_part:
            surface.blit(self.sprites[0], (self.x_first_part, self.y))
            self.x_first_part += 8
        else:
            if self.x_second_part >= self.final_player_position_second_part:
                surface.blit(self.sprites[1], (self.x_second_part, self.y))
                self.need_to_show_pokeball = True
                self.x_second_part -= 3
                self.pokeball_x -= 3
            else:
                if self.x_third_part >= self.final_player_position_third_part:
                    surface.blit(self.sprites[2], (self.x_third_part, self.y))
                    self.x_third_part -= 3
                    self.pokeball_x -= 3
                else:
                    if self.x_fourth_part >= self.final_player_position_fourth_part:
                        surface.blit(self.sprites[3], (self.x_fourth_part, self.y))
                        self.x_fourth_part -= 3
                        self.pokeball_x -= 3
                    else:
                        self.isFinished = True


class ListenableTextDisplay(ScreenAnimation):

    def __init__(self, message: list[str, str]):
        super(ListenableTextDisplay, self).__init__()
        self.text_box = text_box.TextBox(message)

        self.arrow = pygame.transform.scale(
            pygame.transform.rotate(pygame.image.load(os.path.join(config.image, "ui/arrow.png")), -90), (12, 14))
        if message[1] == "":
            coordinate = self.text_box.coordinate[0]
            self.arrow_x_coordinate = self.text_box.font.size(message[0])[0] + coordinate[0]
            self.arrow_y_coordinate = coordinate[1]
        else:
            coordinate = self.text_box.coordinate[1]
            self.arrow_x_coordinate = self.text_box.font.size(message[1])[0] + coordinate[0]
            self.arrow_y_coordinate = coordinate[1]

        self.arrow_animation_x = self.arrow_x_coordinate
        self.arrow_animation_y = self.arrow_y_coordinate
        self.user_input = False

    def update(self, surface):
        self.text_box.draw(surface)
        surface.blit(self.arrow, (self.arrow_animation_x, self.arrow_animation_y))
        self.arrow_animation_y += 0.12
        if self.arrow_animation_y - self.arrow_y_coordinate > 5:
            self.arrow_animation_y = self.arrow_y_coordinate
        self.listen_key()
        if self.user_input:
            self.isFinished = True

    def listen_key(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_n]:
            self.user_input = True


class ScreenAnimationManager:

    def __init__(self) -> None:
        self.animation_queue = []

    def get_current_animation(self) -> ScreenAnimation:
        if not len(self.animation_queue) == 0:
            return self.animation_queue[len(self.animation_queue) - 1]

    def pop_current_animation(self) -> None:
        self.animation_queue.pop()

    def have_animation(self) -> bool:
        return not len(self.animation_queue) == 0

    def add_animation(self, animation) -> None:
        self.animation_queue.insert(0, animation)
