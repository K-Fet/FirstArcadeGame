import arcade
from data import *

class player(arcade.Sprite):
	def __init__(self):
		super().__init__("Image/kfet.png",SPRITE_SCALING_PLAYER)

