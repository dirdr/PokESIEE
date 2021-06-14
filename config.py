import os
import inspect
# screen
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
# assets
scriptPATH = os.path.abspath(inspect.getsourcefile(
    lambda: 0))  # compatible interactive Python Shell
scriptDIR = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR, "data")
map_assets = os.path.join(scriptDIR, "map")

# Player constant
PLAYER_VELOCITY = 1

PLAYER_MAX_HEIGHT = 22
PLAYER_MAX_WIDTH = 15
PLAYER_SCALED_HEIGHT = 2*PLAYER_MAX_HEIGHT
PLAYER_SCALED_WIDTH = 2*PLAYER_MAX_WIDTH
PLAYER_OFFSET_FOOT = 20


PLAYER_STATE_IDLE = 0
PLAYER_STATE_MOVING = 1

TILE_SIZE_SCALED = 32

# Map

MAP_WIDTH = 640
MAP_HEIGHT = 960


#color
BLACK = (0, 0, 0)


