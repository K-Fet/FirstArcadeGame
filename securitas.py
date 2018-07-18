import arcade
from MyGame import *

class securitas(arcade.Sprite):
	def __init__(self,scale):
		super().__init__("Image/secu.png",scale)
	def update(self):
		super().update()
		if self.center_x < LEFT_LIMIT:
			self.center_x = RIGHT_LIMIT
		if self.center_x > RIGHT_LIMIT:
			self.center_x = LEFT_LIMIT
		if self.center_y > TOP_LIMIT:
			self.center_y = BOTTOM_LIMIT
		if self.center_y < BOTTOM_LIMIT:
			self.center_y = TOP_LIMIT
