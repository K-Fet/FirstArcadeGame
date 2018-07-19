import arcade
from MyGame import *
from data import *

class bier(arcade.Sprite):
	def __init__(self):
		super().__init__("Image/bier.png",SPRITE_SCALING_BIER)
		self.center_x=random.randrange(SCREEN_WIDTH)
		self.center_y=random.randrange(SCREEN_HEIGHT)