import math

#game settings
RES = WIDTH, HEIGHT = 1600, 900
FPS = 60

PLAYER_POS = 1.5, 5  # position of player on the map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.04
PLAYER_ROT_SPEED = 0.04

#raycast settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS =  NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20