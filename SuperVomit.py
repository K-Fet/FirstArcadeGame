import arcade
from data import *

class SuperVomit(arcade.Sprite):
	def __init__(self, position_x, position_y, direction_x, direction_y, power):
		super().__init__("img/vomit.png",SPRITE_SCALING_VOMIT)
		self.power = power
		self.center_x = position_x
		self.center_y = position_y
		self.change_x = direction_x * SUPER_VOMIT_PERCENT_SPEED
		self.change_y = direction_y * SUPER_VOMIT_PERCENT_SPEED
		self.life=5
