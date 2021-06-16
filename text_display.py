import pygame
import config
import os


class TextDisplay:

    def __init__(self, ) -> None:
        pygame.font.init()
        self.font = pygame.font.Font(os.path.join(config.font, "game_font.ttf"), 16)
        self.timer = 0
        self.zone = (15, 235)

    def box_display_text(self, text: str, surface):
        temp_surface = (self.font.render(text, False, (0, 0, 0)))
        surface.blit(temp_surface, self.zone)
