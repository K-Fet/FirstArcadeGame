import arcade
from data import *

class securitas(arcade.Sprite):
	def __init__(self,center_x,center_y):
		super().__init__("img/securitas.png",SPRITE_SCALING_SECURITAS)
		self.center_x=center_x
		self.center_y=center_y
