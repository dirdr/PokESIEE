import pygame
import os

# this class contains many useful animation for battle etc
import config
import spritesheet


class ScreenAnimation:

    def __init__(self) -> None:
        self.isFinished = False
        self.alpha = 300


class ScreenFade(ScreenAnimation):

    def __init__(self, speed: int) -> None:
        super(ScreenFade, self).__init__()
        self.fade_speed = speed
        # logic

    def update(self, surface):
        if self.alpha >= 0:
            print(self.alpha)
            surface.set_alpha(self.alpha)
            self.alpha -= self.fade_speed
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

    def __init__(self):
        super(RectAnimation, self).__init__()
        self.timer = 0
        self.rect_length_bottom = config.SCREEN_HEIGHT / 2
        self.rect_length_upper = config.SCREEN_HEIGHT / 2

    def update(self, surface: pygame.Surface):
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


class PlayerEnterBattle(ScreenAnimation):

    def __init__(self):
        super(PlayerEnterBattle, self).__init__()
        self.player_sprite_sheet = pygame.image.load(os.path.join(config.assets, "player_spritesheet.png"))
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
        self.pokeball_x = self.pokeball_base_x
        self.pokeball_base_y = 165
        self.pokeball_y = self.pokeball_base_y
        self.need_to_show_pokeball = False

    def load_sprites(self):

        x_temp = 228

        for i in range(0, 4):
            sub_image = spritesheet.pick_image(self.player_sprite_sheet, x_temp, 0, 128, 128)
            self.sprites.append(sub_image)
            x_temp += 128
        self.sprites.append(
            pygame.transform.scale(pygame.image.load(os.path.join(config.assets, "poke_ball.png")), (20, 25)))

    def update(self, surface):

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


class ScreenAnimationManager:

    def __init__(self):
        self.animation_queue = []

    def get_current_animation(self):
        if not len(self.animation_queue) == 0:
            return self.animation_queue[len(self.animation_queue) - 1]

    def pop_current_animation(self):
        self.animation_queue.pop()

    def have_animation(self):
        return not len(self.animation_queue) == 0

    def add_animation(self, animation):
        self.animation_queue.insert(0, animation)
