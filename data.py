# Constant variables
SCREEN_WIDTH=1280
SCREEN_HEIGHT=720
SPRITE_SCALING_PLAYER=0.35
FULLSCREEN = False

BORDERS_OFFSET = 15

#MOVEMENT SPEED
MOVEMENT_SPEED = 5
SECURITAS_SPEED = 2
ANGRY_SECURITAS_SPEED = 3

# Angry securitas BAC
SECURITAS_RADIUS = 400

# Define the duration (sec) of the CAN'T_MOVE capability of the player/securitas.
# This capability is set to True when the player/securitas hit a vomit.
TIME_STATIC=3 

# Define the duration (sec) of the invincible capability of the player.
# This capability is set to True when the player vomit.
# The player is can't hit a vomit when he is invincible 
TIME_INVINCIBLE=1

SPRITE_SCALING_BEER=0.100
SPRITE_SCALING_SECURITAS=0.35
SPRITE_SCALING_VOMIT=0.2

#BEER GENERATION COEFF
BEER_GENERATION_COEFF = 20
BEER_BOOST_COEFF = 5
BEER_DELAY = 35 # not in second, probability that a beer appear on a tick is 1/BEER_DELAY 
MAX_BAC_BOOST = 0
SECOND_STEP_MAX_BAC_BOOST = 3

TOTAL_TIME_SECOND_STEP = 30

# Number of beer to set the player drunk
DRUNK_LEVEL_PLAYER = 5

RIGHT=1
LEFT=2
UP=3
DOWN=4

HIGHSCORE_FILE="highscore"

MAP1_POINT_LIST = ((183,720),(1206,720),(1226,586),(1150,493),(1106,365),(1100,320),(1093,146),(1100,20),(986,20),(986,186),(926,186),(926,120),(823,120),(820,186),(160,166),(183,720))
