
import pygame
from entity import Entity
import spritesheet
import config
from draw_area import DrawArea
from game_map import GameMap
import numpy


class Player(Entity):

    # constructor
    def __init__(self, area: DrawArea, game_map: GameMap) -> None:
        super(Player, self).__init__(10, 10, 'player_spritesheet.png')

        # player screen position
        self.y_screen = config.SCREEN_HEIGHT / 2 - config.PLAYER_SCALED_HEIGHT / 2
        self.x_screen = config.SCREEN_WIDTH / 2 - config.PLAYER_SCALED_WIDTH / 2

        # player current logical tile
        self.current_tile_x = 5
        self.current_tile_y = 6

        # player logical position
        self.x_logical_decor = self.current_tile_x * config.TILE_SIZE_SCALED
        self.y_logical_decor = self.current_tile_y * config.TILE_SIZE_SCALED + config.PLAYER_OFFSET_FOOT

        # render x and y coordinates (smooth animation)
        self.x_render = self.x_logical_decor
        self.y_render = self.y_logical_decor

        # animation coordinates from source to destination
        self.src_x = self.x_logical_decor
        self.src_y = self.y_logical_decor
        self.dest_x = self.x_logical_decor
        self.dest_y = self.y_logical_decor

        # animation timer
        self.animation_timer = 0
        self.ANIMATION_TIME = 0.25

        # ref variables
        self.area = area
        self.game_map = game_map

        # configuration de la zone d'affichage

        self.area.x = self.x_render - self.x_screen
        self.area.y = self.y_render - self.y_screen

        # misc
        self.animation = {}
        self.direction = ''
        self.last_direction = ''
        self.state = config.PLAYER_STATE_IDLE
        self.load()
        self.current_sprite = self.animation['MoveDownWalk'][0]

        self.REFACE_TIME = 0.1
        self.facing_timer = self.REFACE_TIME
        self.facing_dir = 'DOWN'

        self.running = False
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.walk_cool_down = 0
        self.walk_delay = 0.25
        self.time = self.time = int(pygame.time.get_ticks() / 170)

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

    def initialize_move(self, old_x: int, old_y: int, dest_x: int, dest_y: int) -> None:

        self.src_x = old_x
        self.src_y = old_y
        self.dest_x = old_x + dest_x
        self.dest_y = old_y + dest_y
        self.x_render = old_x
        self.y_render = old_y
        self.animation_timer = 0
        self.state = config.PLAYER_STATE_MOVING


    def finish_move(self):
        self.state = config.PLAYER_STATE_IDLE

    # update class method
    def update(self) -> None:
        self.clock_update()
        self.handle_key()
        self.update_position()
        self.select_sprite()

    def clock_update(self):
        self.dt = self.clock.tick() / 1000

    def update_position(self):
        if self.state == config.PLAYER_STATE_MOVING:
            self.animation_timer += self.dt
            alpha = self.animation_timer / self.ANIMATION_TIME
            xp = [0, 1]
            fpx = [self.src_x, self.dest_x]
            fpy = [self.src_y, self.dest_y]
            self.x_logical_decor = self.current_tile_x * config.TILE_SIZE_SCALED
            self.y_logical_decor = self.current_tile_y * config.TILE_SIZE_SCALED + config.PLAYER_OFFSET_FOOT
            self.x_render = numpy.interp(alpha, xp, fpx)
            self.y_render = numpy.interp(alpha, xp, fpy)
            self.area.x = self.x_render - self.x_screen
            self.area.y = self.y_render - self.y_screen
            if self.animation_timer > self.ANIMATION_TIME:
                self.state = config.PLAYER_STATE_IDLE

    # Global load function
    def load(self) -> None:
        self.load_animation()

    def go_up(self) -> None:

        self.current_tile_y -= 1
        self.initialize_move(self.x_logical_decor, self.y_logical_decor, 0,
                             -32)

    def go_down(self) -> None:

        self.current_tile_y += 1
        self.initialize_move(self.x_logical_decor, self.y_logical_decor, 0,
                             32)

    def go_right(self) -> None:

        self.current_tile_x += 1
        self.initialize_move(self.x_logical_decor, self.y_logical_decor, 32,
                             0)

    def go_left(self) -> None:

        self.current_tile_x -= 1
        self.initialize_move(self.x_logical_decor, self.y_logical_decor, -32,
                             0)

    def check_can_go_right(self) -> bool:
        map_limit = int(self.game_map.width/16)
        x_tile_to_look = self.current_tile_x + 1
        y_tile_to_look = self.current_tile_y + 1
        print(self.current_tile_y)
        if x_tile_to_look >= map_limit:
            return False
        else:
            if self.game_map.map_grid[y_tile_to_look][x_tile_to_look] == 'c':
                return False
            else:
                return True

    def check_can_go_down(self) -> bool:
        map_limit = int(self.game_map.height/16)
        y_tile_to_look = self.current_tile_y + 2
        if y_tile_to_look >= map_limit:
            return False
        else:
            if self.game_map.map_grid[y_tile_to_look][self.current_tile_x] == 'c':
                return False
            else:
                return True

    def check_can_go_up(self) -> bool:
        map_limit = 0
        y_tile_to_look = self.current_tile_y
        if y_tile_to_look <= map_limit - 1:
            return False
        else:
            if self.game_map.map_grid[y_tile_to_look][self.current_tile_x] == 'c':
                return False
            else:
                return True

    def check_can_go_left(self) -> bool:
        map_limit = -1
        x_tile_to_look = self.current_tile_x - 1
        y_tile_to_look = self.current_tile_y + 1
        if x_tile_to_look <= map_limit:
            return False
        else:
            if self.game_map.map_grid[y_tile_to_look][x_tile_to_look] == 'c':
                return False
            else:
                return True

    def handle_key(self) -> None:

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_n]:
            self.running = True
        else:
            self.running = False

        self.last_direction = self.direction
        self.walk_cool_down -= self.dt

        if self.walk_cool_down <= 0:

            if keys_pressed[pygame.K_UP]:
                self.direction = 'UP'
                if self.check_can_go_up():
                    self.go_up()
                    self.walk_cool_down = self.walk_delay

            elif keys_pressed[pygame.K_DOWN]:
                self.direction = 'DOWN'
                if self.check_can_go_down():
                    self.go_down()
                    self.walk_cool_down = self.walk_delay

            elif keys_pressed[pygame.K_LEFT]:
                self.direction = 'LEFT'
                if self.check_can_go_left():
                    self.go_left()
                    self.walk_cool_down = self.walk_delay

            elif keys_pressed[pygame.K_RIGHT]:
                self.direction = 'RIGHT'
                if self.check_can_go_right():
                    self.go_right()
                    self.walk_cool_down = self.walk_delay
            else:
                self.direction = 'NONE'

    def select_sprite(self) -> None:

        if self.running:
            self.time = int(pygame.time.get_ticks() / 100)
        else:
            self.time = int(pygame.time.get_ticks() / 170)

        if self.direction == 'UP':
            if self.running:
                self.current_sprite = self.animation['MoveUpRun'][self.time % len(self.animation['MoveUpRun'])]
            else:
                self.current_sprite = self.animation['MoveUpWalk'][self.time % len(self.animation['MoveUpWalk'])]

        if self.direction == 'DOWN':
            if self.running:
                self.current_sprite = self.animation['MoveDownRun'][self.time % len(self.animation['MoveDownRun'])]
            else:
                self.current_sprite = self.animation['MoveDownWalk'][self.time % len(self.animation['MoveDownWalk'])]

        if self.direction == 'RIGHT':
            if self.running:
                self.current_sprite = self.animation['MoveRightRun'][self.time % len(self.animation['MoveRightRun'])]
            else:
                self.current_sprite = self.animation['MoveRightWalk'][self.time % len(self.animation['MoveRightWalk'])]
        if self.direction == 'LEFT':
            if self.running:
                self.current_sprite = self.animation['MoveLeftRun'][self.time % len(self.animation['MoveLeftRun'])]
            else:
                self.current_sprite = self.animation['MoveLeftWalk'][self.time % len(self.animation['MoveLeftWalk'])]

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
        hit_box = (self.x_screen, self.y_screen, config.PLAYER_SCALED_WIDTH, config.PLAYER_SCALED_HEIGHT)
        x_coordinate = (self.x_screen, self.y_screen, config.PLAYER_SCALED_WIDTH, config.PLAYER_SCALED_HEIGHT)
        screen_middle = (config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2, 1, 1)
        screen.blit(pygame.transform.scale2x(self.current_sprite), (self.x_screen, self.y_screen))
        #pygame.draw.rect(screen, (255, 0, 0), hit_box)
        # pygame.draw.rect(screen, (250, 250, 0), screen_middle)
