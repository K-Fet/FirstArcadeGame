import arcade
from data import *

class vomit(arcade.Sprite):
	def __init__(self,position_x,position_y):
		super().__init__("img/vomit.png",SPRITE_SCALING_VOMIT)
		self.center_x=position_x
		self.center_y=position_y
		self.life=15.0

		
