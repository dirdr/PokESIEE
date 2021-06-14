import pygame
import config
import os


class Entity:

    # entity constructor
    def __init__(self, width: int, height: int, image_path: str) -> None:
        self.width = width
        self.height = height
        self.imagePath = image_path
        self.image = pygame.image.load(os.path.join(config.assets, self.imagePath))
        self.scaled = pygame.transform.scale2x(self.image)



