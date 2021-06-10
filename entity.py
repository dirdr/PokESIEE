import pygame
import config
import os


class entity:

    # entity constructor
    def __init__(self, x: int, y: int, width: int, height: int, imagePath: str):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.imagePath = imagePath

    # load an entity image from its imagePath

    def load_image(self):
        return pygame.image.load(os.path.join((config.assets, self.imagePath)))
