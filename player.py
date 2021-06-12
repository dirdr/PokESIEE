import pygame
from entity import Entity
import spritesheet
import config
from draw_area import DrawArea
from game_map import GameMap


class Player(Entity):

    # constructor
    def __init__(self, x: int, y: int, area: DrawArea, map: GameMap) -> None:
        super(Player, self).__init__(10, 10, 'player_spritesheet.png')
        self.x = x
        self.y = y
        self.animation = {}
        self.direction = ''
        self.last_direction = ''
        self.running = False
        self.load()
        self.current_sprite = self.animation['MoveDownWalk'][0]
        self.area = area
        self.map = map

    def load_animation(self) -> None:
        # those array store the player animation
        width = 15
        y_temp = 0

        self.animation['MoveUpRun'] = []
        self.animation['MoveUpWalk'] = []

        self.animation['MoveDownWalk'] = []
        self.animation['MoveDownRun'] = []

        self.animation['MoveLeftWalk'] = []
        self.animation['MoveLeftRun'] = []

        self.animation['MoveRightWalk'] = []
        self.animation['MoveRightRun'] = []

        height_tab = [22, 22, 22, 20, 20, 21]
        for i in range(0, 3):
            self.animation['MoveDownWalk'].append(spritesheet.pick_image(self.image, 0, y_temp, width, height_tab[i]))
            y_temp += height_tab[i]

        for i in range(3, 6):
            self.animation['MoveDownRun'].append(spritesheet.pick_image(self.image, 0, y_temp, width, height_tab[i]))
            y_temp += height_tab[i]

        y_temp = 0
        for i in range(0, 3):
            self.animation['MoveUpWalk'].append(spritesheet.pick_image(self.image, 15, y_temp, width, height_tab[i]))
            y_temp += height_tab[i]
        for i in range(3, 6):
            self.animation['MoveUpRun'].append(spritesheet.pick_image(self.image, 15, y_temp, width, height_tab[i]))
            y_temp += height_tab[i]

        y_temp = 0

        height_tab = [22, 22, 21, 21, 21, 20]

        for i in range(0, 3):
            image = spritesheet.pick_image(self.image, 30, y_temp, width, height_tab[i])
            self.animation['MoveLeftWalk'].append(image)
            self.animation['MoveRightWalk'].append(pygame.transform.flip(image, True, False))
            y_temp += height_tab[i]

        for i in range(3, 6):
            image = spritesheet.pick_image(self.image, 30, y_temp, width, height_tab[i])
            self.animation['MoveLeftRun'].append(image)
            self.animation['MoveRightRun'].append(pygame.transform.flip(image, True, False))
            y_temp += height_tab[i]

    # update class method
    def update(self) -> None:
        self.handle_key()
        self.select_sprite()

    # Global load function
    def load(self) -> None:
        self.load_animation()

    def check_oob_up(self) -> bool:
        pass

    def check_oob_down(self) -> bool:
        pass

    def check_oob_left(self) -> bool:
        pass

    def check_oob_right(self) -> bool:
        pass

    def go_up(self) -> None:
        self.direction = 'UP'
        self.area.y -= config.PLAYER_VELOCITY

    def go_down(self) -> None:
        self.direction = 'DOWN'
        self.area.y += config.PLAYER_VELOCITY

    def go_right(self) -> None:
        self.direction = 'RIGHT'
        self.area.x += config.PLAYER_VELOCITY

    def go_left(self) -> None:
        self.direction = 'LEFT'
        self.area.x -= config.PLAYER_VELOCITY

    def check_can_go_up(self):
        pass

    def check_can_go_down(self):
        pass

    def check_can_go_right(self):
        pass

    def check_can_go_left(self):
        pass




    def handle_key(self) -> None:

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_n]:
            self.running = True
        else:
            self.running = False

        self.last_direction = self.direction

        if keys_pressed[pygame.K_UP]:
            self.go_up()

        elif keys_pressed[pygame.K_DOWN]:
            self.go_down()

        elif keys_pressed[pygame.K_LEFT]:
            self.go_left()

        elif keys_pressed[pygame.K_RIGHT]:
            self.go_right()
        else:
            self.direction = 'NONE'

    def select_sprite(self) -> None:

        if self.running:
            time = int(pygame.time.get_ticks() / 100)
            config.PLAYER_VELOCITY = 2
        else:
            time = int(pygame.time.get_ticks() / 170)
            config.PLAYER_VELOCITY = 1

        if self.direction == 'UP':
            if self.running:
                self.current_sprite = self.animation['MoveUpRun'][time % len(self.animation['MoveUpRun'])]
            else:
                self.current_sprite = self.animation['MoveUpWalk'][time % len(self.animation['MoveUpWalk'])]

        if self.direction == 'DOWN':
            if self.running:
                self.current_sprite = self.animation['MoveDownRun'][time % len(self.animation['MoveDownRun'])]
            else:
                self.current_sprite = self.animation['MoveDownWalk'][time % len(self.animation['MoveDownWalk'])]

        if self.direction == 'RIGHT':
            if self.running:
                self.current_sprite = self.animation['MoveRightRun'][time % len(self.animation['MoveRightRun'])]
            else:
                self.current_sprite = self.animation['MoveRightWalk'][time % len(self.animation['MoveRightWalk'])]
        if self.direction == 'LEFT':
            if self.running:
                self.current_sprite = self.animation['MoveLeftRun'][time % len(self.animation['MoveLeftRun'])]
            else:
                self.current_sprite = self.animation['MoveLeftWalk'][time % len(self.animation['MoveLeftWalk'])]

        if self.direction == 'NONE':
            if self.last_direction == 'RIGHT':
                self.current_sprite = self.animation['MoveRightWalk'][0]
            if self.last_direction == 'LEFT':
                self.current_sprite = self.animation['MoveLeftWalk'][0]
            if self.last_direction == 'UP':
                self.current_sprite = self.animation['MoveUpWalk'][0]
            if self.last_direction == 'DOWN':
                self.current_sprite = self.animation['MoveDownWalk'][0]

    # draw class method
    def draw(self, screen):
        screen.blit(pygame.transform.scale2x(self.current_sprite), (self.x, self.y))
