import pygame


# this class contains many useful animation for battle etc
import config


class ScreenAnimation:

    def __init__(self) -> None:
        self.isFinished = False
        self.alpha = 0


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


class ScreenFade(ScreenAnimation):

    def __init__(self, speed: int) -> None:
        super(ScreenFade, self).__init__()
        self.alpha = 300
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
        super().__init__()
        self.fade_speed = 40
        self.number_of_fade = 3













