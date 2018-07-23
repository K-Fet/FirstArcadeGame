import arcade
from data import *

class player(arcade.Sprite):
	def __init__(self,center_x,center_y):
		super().__init__("img/player.png",SPRITE_SCALING_PLAYER)
		self.center_x=center_x
		self.center_y=center_y
		self.BAC= None
		self.can_move=None
		self.static_time=None
		self.username="Bd"

	def update(self, delta_time):
		## reset the change_x before updating if player is on screen limit
		if self.can_move == False:
			if self.static_time <= 0:
				self.can_move=True
			else :
				self.static_time-=delta_time
		