import pygame
import config
import os


class Entity:

    # entity constructor
    def __init__(self,width: int, height: int, imagePath: str):
        self.width = width
        self.height = height
        self.imagePath = imagePath

    # load an entity image from its imagePath

    def load_image(self):
        return pygame.image.load(os.path.join((config.assets, self.imagePath)))


    