import os
import inspect

# screen
import pygame.time

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

# assets
scriptPATH = os.path.abspath(inspect.getsourcefile(
    lambda: 0))  # compatible interactive Python Shell
scriptDIR = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR, "data")
map_assets = os.path.join(scriptDIR, "map")
font = os.path.join(scriptDIR, "font")

# Player constant
PLAYER_VELOCITY = 1

PLAYER_MAX_HEIGHT = 22
PLAYER_MAX_WIDTH = 15
PLAYER_SCALED_HEIGHT = 2 * PLAYER_MAX_HEIGHT
PLAYER_SCALED_WIDTH = 2 * PLAYER_MAX_WIDTH
PLAYER_OFFSET_FOOT = 20

# player states
PLAYER_STATE_IDLE = 0
PLAYER_STATE_MOVING = 1
PLAYER_STATE_REFACING = 2
PLAYER_REFACE_TIMING = 0.15

PLAYER_TIME_PER_TILE_WALKING = 0.4
PLAYER_TIME_PER_TILE_RUNNING = 0.25
PLAYER_TIME_PER_TILE_BIKING = 0.1

# player mode
PLAYER_MODE_WALK = 0
PLAYER_MODE_RUN = 1
PLAYER_MODE_BIKE = 2

TILE_SIZE_SCALED = 32

# Map

MAP_WIDTH = 640
MAP_HEIGHT = 960

# color
BLACK = (0, 0, 0)

# Main_Loop
MAIN_LOOP_DOWN = False

# clock
GAME_CLOCK = pygame.time.Clock()

COOL_DOWN_WALKING = 0.25
COOL_DOWN_RUNNING = 1
dt = 1 / 60
FIND_POKEMON_CHANCE_BOUND = 1

GAME_STATE_EXPLORATION = 0
GAME_STATE_ANIMATION = 1
GAME_STATE_BATTLE = 2

TYPE_BATTLE_WILD_POKEMON = 0
TYPE_BATTLE_TRAINER = 1

