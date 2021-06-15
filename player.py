import pygame
from entity import Entity
import spritesheet
import config
from draw_area import DrawArea
from game_map import GameMap
import numpy
from direction import Directions as dir
import direction
from assets import PlayerAnimations


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
        # ref variables
        self.area = area
        self.game_map = game_map
        # screen blit coordinates configuration
        self.area.x = self.x_render - self.x_screen
        self.area.y = self.y_render - self.y_screen


        # misc
        self.animation = PlayerAnimations(self.image)

        # direction

        self.directionPressed = {direction.Directions.NORTH: False, direction.Directions.SOUTH: False,
                                 direction.Directions.EAST: False, direction.Directions.WEST: False}

        self.directionPressedTimer = {direction.Directions.NORTH: 0, direction.Directions.SOUTH: 0,
                                      direction.Directions.EAST: 0, direction.Directions.WEST: 0}

        # at the game start, the player is facing down
        self.facing = direction.Directions.SOUTH

        self.state = config.PLAYER_STATE_IDLE
        self.current_mode = config.PLAYER_MODE_WALK
        self.next_mode = config.PLAYER_MODE_WALK

        # Number of second the tile crossing animation is gonna be
        self.time_per_tile_walking = float(0.4)
        self.time_per_tile_running = float(0.15)
        self.time_per_tile_biking = float(0.10)

        self.time_per_tile = self.time_per_tile_walking
        self.cool_down = config.COOL_DOWN_WALKING
        self.request_move_frame = True

    # initialize all the move variables

    def initialize_move(self, mov_dir: direction.Direction) -> None:
        self.facing = mov_dir
        self.src_x = self.x_logical_decor
        self.src_y = self.y_logical_decor
        self.dest_x = self.x_logical_decor + mov_dir.dx * config.TILE_SIZE_SCALED
        self.dest_y = self.y_logical_decor + mov_dir.dy * config.TILE_SIZE_SCALED
        self.x_render = self.x_logical_decor
        self.y_render = self.y_logical_decor
        self.animation_timer = 0
        self.state = config.PLAYER_STATE_MOVING
        self.current_mode = self.next_mode

    # finish the animation and reset all the move variables
    def finish_move(self):
        self.state = config.PLAYER_STATE_IDLE
        self.x_logical_decor = self.dest_x
        self.y_logical_decor = self.dest_y
        self.src_x = 0
        self.src_y = 0
        self.dest_x = 0
        self.dest_y = 0

    def update(self):
        self.update_control(config.dt)
        self.update_movement(config.dt)
        self.update_coordinates()

    def update_control(self, dt: float):

        if self.directionPressed[dir.NORTH]:
            self.update_direction(direction.Directions.NORTH, dt)
            return
        if self.directionPressed[dir.SOUTH]:
            self.update_direction(direction.Directions.SOUTH, dt)
            return
        if self.directionPressed[dir.EAST]:
            self.update_direction(direction.Directions.EAST, dt)
            return
        if self.directionPressed[dir.WEST]:
            self.update_direction(direction.Directions.WEST, dt)
            return

    def release_direction(self, mov_dir) -> None:
        self.directionPressed[mov_dir] = False
        self.consider_reface(mov_dir)
        self.directionPressedTimer[mov_dir] = 0

    def update_direction(self, mov_dir: direction.Direction, dt: float) -> None:
        self.directionPressedTimer[mov_dir] += dt
        self.consider_movement(mov_dir)

    def consider_movement(self, mov_dir: direction.Direction) -> None:
        if self.directionPressedTimer[mov_dir] > config.PLAYER_REFACE_TIMING:
            self.move(mov_dir)

    def consider_reface(self, mov_dir: direction.Direction) -> None:
        if self.directionPressedTimer[mov_dir] < config.PLAYER_REFACE_TIMING:
            self.reface(mov_dir)

    # player refacing
    def reface(self, mov_dir) -> bool:
        # cannot refacing if not IDLE
        if not self.state == config.PLAYER_STATE_IDLE:
            return False
        # can't reface in the player current direction
        if self.facing == mov_dir:
            return True
        # reface
        self.facing = mov_dir
        self.state = config.PLAYER_STATE_REFACING
        self.animation_timer = 0
        return True

    def move(self, mov_dir: direction.Direction) -> bool:
        if self.state == config.PLAYER_STATE_MOVING:
            if self.facing == mov_dir:
                self.request_move_frame = True
            return False

        if self.gonna_be_oob(mov_dir):
            self.reface(mov_dir)
            return False
        if not self.can_go_next_tile(mov_dir):
            self.reface(mov_dir)
            return False

        self.initialize_move(mov_dir)
        self.current_tile_x += mov_dir.dx
        self.current_tile_y += mov_dir.dy

    def gonna_be_oob(self, mov_dir: direction.Direction) -> bool:

        map_limit_width = int(self.game_map.width/16)
        map_limit_height = int(self.game_map.height/16)
        tile_to_look_x = self.current_tile_x + mov_dir.dx
        tile_to_look_y = self.current_tile_y + mov_dir.dy + 1

        if tile_to_look_x >= map_limit_width or tile_to_look_x < 0:
            return True
        elif tile_to_look_y >= map_limit_height or tile_to_look_y < 0:
            return True
        else:
            return False

    def can_go_next_tile(self, mov_dir: direction.Direction) -> bool:
        tile_to_look_x = self.current_tile_x + mov_dir.dx
        tile_to_look_y = self.current_tile_y + 1 + mov_dir.dy
        if self.game_map.map_grid[tile_to_look_y][tile_to_look_x] == 'c':
            return False
        else:
            return True

    def update_coordinates(self):
        self.area.x = self.x_render - self.x_screen
        self.area.y = self.y_render - self.y_screen

    # Player update function
    def update_movement(self, dt):

        if self.state == config.PLAYER_STATE_MOVING:

            self.animation_timer += dt

            if self.current_mode == config.PLAYER_MODE_WALK:
                time_per_tile = config.PLAYER_TIME_PER_TILE_WALKING
            elif self.current_mode == config.PLAYER_MODE_RUN:
                time_per_tile = config.PLAYER_TIME_PER_TILE_RUNNING
            else:
                time_per_tile = config.PLAYER_TIME_PER_TILE_BIKING
            alpha = self.animation_timer / time_per_tile
            xp = [0, 1]
            fpx = [self.src_x, self.dest_x]
            fpy = [self.src_y, self.dest_y]
            self.x_render = numpy.interp(alpha, xp, fpx)
            self.y_render = numpy.interp(alpha, xp, fpy)
            if self.animation_timer >= time_per_tile:
                self.finish_move()

    def select_sprite(self) -> pygame.Surface:

        if self.current_mode == config.PLAYER_MODE_WALK:

            time = int(pygame.time.get_ticks()/170)

            if self.state == config.PLAYER_STATE_MOVING:
                return self.animation.walking[self.facing][time % len(self.animation.walking[self.facing])]
            else:
                return self.animation.walking[self.facing][0]

        elif self.current_mode == config.PLAYER_MODE_RUN:

            time = int(pygame.time.get_ticks()/120)
            if self.state == config.PLAYER_STATE_MOVING:
                return self.animation.running[self.facing][time % len(self.animation.running[self.facing])]
            else:
                return self.animation.running[self.facing][0]

    # draw class method
    def draw(self, screen) -> None:
        screen.blit(self.select_sprite(), (self.x_screen, self.y_screen))
