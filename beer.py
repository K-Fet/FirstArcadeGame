import arcade
from data import *

class beer(arcade.Sprite):
	def __init__(self,center_x,center_y):
		super().__init__("img/beer.png",SPRITE_SCALING_BEER)
		self.center_x=center_x
		self.center_y=center_y
