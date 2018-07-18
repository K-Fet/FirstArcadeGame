import arcade
from MyGame import *
import math

class player(arcade.Sprite):
	def __init__(self,scale):
		super().__init__("Image/kfet.png",scale)