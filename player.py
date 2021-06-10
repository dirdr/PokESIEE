import pygame
from entity import Entity
import spritesheet
import config


class Player(Entity):

    # constructor
    def __init__(self, x: int, y: int):
        super(Player, self).__init__(10, 10, 'player_spritesheet.png')
        self.x = x
        self.y = y
        self.animation = {}
        self.direction = {}
        self.running = False
        self.load()
        self.current_sprite = self.animation['MoveDown'][0]

    def load_animation(self) -> None:
        # those array store the player animation
        width = 15
        height = 22
        y_temp = 0
        self.animation['MoveUp'] = []
        self.animation['MoveDown'] = []
        self.animation['MoveLeft'] = []
        self.animation['MoveRight'] = []

        height_tab = [22, 22, 22, 20, 20, 21]
        for i in range(0, 6):
            self.animation['MoveDown'].append(spritesheet.pick_image(self.image, 0, y_temp, width, height_tab[i]))
            y_temp += height_tab[i]

        y_temp = 0
        for i in range(0, 6):
            self.animation['MoveUp'].append(spritesheet.pick_image(self.image, 15, y_temp, width, height_tab[i]))
            y_temp += height_tab[i]

        y_temp = 0

        height_tab = [22, 22, 21, 21, 21, 20]
        for i in range(0, 6):
            image = spritesheet.pick_image(self.image, 30, y_temp, width, height_tab[i])
            self.animation['MoveLeft'].append(image)
            self.animation['MoveRight'].append(pygame.transform.flip(image, True, False))
            y_temp += height_tab[i]

    # update class method
    def update(self) -> None:
        self.handle_key()
        self.select_sprite()

    # Global load function
    def load(self) -> None:
        self.load_animation()
        self.clear_direction()

    def clear_direction(self) -> None:
        self.direction['RIGHT'] = False
        self.direction['LEFT'] = False
        self.direction['DOWN'] = False
        self.direction['UP'] = False
        self.direction['NONE'] = False

    def handle_key(self) -> None:

        keys_pressed = pygame.key.get_pressed()
        self.clear_direction()

        if keys_pressed[pygame.K_n]:
            self.running = True
        else:
            self.running = False


        if keys_pressed[pygame.K_UP]:
            self.y -= config.PLAYER_VELOCITY
            self.direction['UP'] = True

        elif keys_pressed[pygame.K_DOWN]:
            self.y += config.PLAYER_VELOCITY
            self.direction['DOWN'] = True

        elif keys_pressed[pygame.K_LEFT]:
            self.x -= config.PLAYER_VELOCITY
            self.direction['LEFT'] = True

        elif keys_pressed[pygame.K_RIGHT]:
            self.x += config.PLAYER_VELOCITY
            self.direction['RIGHT'] = True

        else:
            self.direction['NONE'] = True

    def select_sprite(self) -> None:

        if self.running:
            time = int(pygame.time.get_ticks() / 100)
            config.PLAYER_VELOCITY = 4
        else:
            time = int(pygame.time.get_ticks() / 200)
            config.PLAYER_VELOCITY = 2

        if self.direction['UP']:
            self.current_sprite = self.animation['MoveUp'][time % len(self.animation['MoveUp'])]
        if self.direction['DOWN']:
            self.current_sprite = self.animation['MoveDown'][time % len(self.animation['MoveDown'])]
        if self.direction['RIGHT']:
            self.current_sprite = self.animation['MoveRight'][time % len(self.animation['MoveRight'])]
        if self.direction['LEFT']:
            self.current_sprite = self.animation['MoveLeft'][time % len(self.animation['MoveLeft'])]
        if self.direction['NONE']:
            self.current_sprite = self.animation['MoveDown'][0]



    # draw class method
    def draw(self, screen):
        scaled = pygame.transform.scale(self.current_sprite, (20, 30))
        screen.blit(scaled, (self.x, self.y))




