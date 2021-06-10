import pygame
from entity import Entity


class Player(Entity):

    #constructor
    def __init__(self, x, y):
        super.__init__(self, 10, 10, "player_spritesheet.png")
        self.x = x
        self.y = y
        self.image = self.load_image()


    def load_animation(self):
        #those array store the player animation
        self.moveUp = []
        self.moveDown = []
        self.moveLeft = []
        self.moveRight = []
    
    #update class method
    def update(self):
        pass

    #draw class method 
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

