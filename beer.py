import arcade
from data import *
import random

class beer(arcade.Sprite):
	def __init__(self, x=None, y=None):
		if (x == None): x = random.randrange(SCREEN_WIDTH//3, 2 * SCREEN_WIDTH//3)
		if (y == None): y = random.randrange(SCREEN_HEIGHT//3, 2 * SCREEN_HEIGHT//3)
		super().__init__("img/beer.png",SPRITE_SCALING_BEER)
		self.center_x=x
		self.center_y=y
		
