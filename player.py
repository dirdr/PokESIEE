import pygame
from entity import Entity


class Player(Entity):

    #constructor
    def __init__(self):
        super.__init__(self, 10, 10, "player_spritesheet")
    
    #update class method
    def update(self):
        pass

    #draw class method 
    def draw(self, screen):
        pass

