import arcade
from data import *

class player(arcade.Sprite):
	def __init__(self,center_x,center_y):
		super().__init__("img/player.png",SPRITE_SCALING_PLAYER)
		self.center_x=center_x
		self.center_y=center_y
	

