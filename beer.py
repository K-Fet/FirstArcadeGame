import arcade
from data import *
import random

class beer(arcade.Sprite):
	def __init__(self):
		super().__init__("img/beer.png",SPRITE_SCALING_BEER)
		self.center_x=random.randrange(SCREEN_WIDTH)
		self.center_y=random.randrange(SCREEN_HEIGHT)
		
