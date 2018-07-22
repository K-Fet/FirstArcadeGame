import arcade
from data import *

class player(arcade.Sprite):
	def __init__(self,center_x,center_y):
		super().__init__("img/player.png",SPRITE_SCALING_PLAYER)
		self.center_x=center_x
		self.center_y=center_y

	def update(self, screen_width, screen_heigth, disabledKeys):
		## reset the change_x before updating if player is on screen limit
		# if (self.center_x < BORDERS_OFFSET):
		# 	if self.change_x < 0 : self.change_x = 0
		# if (self.center_x > screen_width - BORDERS_OFFSET):
		# 	if self.change_x > 0 : self.change_x = 0
		# if (self.center_y < BORDERS_OFFSET):
		# 	if self.change_y < 0 : self.change_y = 0
		# if (self.center_y > screen_heigth - BORDERS_OFFSET):
		# 	if self.change_y > 0 : self.change_y = 0
		print(disabledKeys)
		if (disabledKeys[0] and self.change_x < 0) : self.change_x = 0
		if (disabledKeys[1] and self.change_x > 0) : self.change_x = 0
		if (disabledKeys[2] and self.change_y > 0) : self.change_y = 0
		if (disabledKeys[3] and self.change_y < 0) : self.change_y = 0


		super().update()
	

