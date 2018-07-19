import arcade
from MyGame import *
import math
from data import *

class player(arcade.Sprite):
	def __init__(self):
		super().__init__("Image/kfet.png",SPRITE_SCALING_PLAYER)
		self.center_x=50
		self.center_y=50