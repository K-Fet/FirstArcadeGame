import arcade
from data import *
import random

class beer(arcade.Sprite):
	def __init__(self, x=random.randrange(SCREEN_WIDTH), y=random.randrange(SCREEN_HEIGHT)):
		super().__init__("img/beer.png",SPRITE_SCALING_BEER)
		self.center_x=x
		self.center_y=y
		
