import arcade
from data import *

class player(arcade.Sprite):
	def __init__(self,filename,center_x,center_y,isDrunk=False):
		super().__init__(filename,SPRITE_SCALING_PLAYER)
		self.center_x=center_x
		self.center_y=center_y
		self.BAC = 0 if isDrunk == False  else DRUNK_LEVEL_PLAYER
		self.isDrunk = isDrunk
		self.isSuperDrunk = False
		self.can_move= True
		self.static_time=0
		self.invincible= False
		self.invincible_time=None
		self.username="Bd"

	def update(self, delta_time):

		# Decrease the static_time attribute by delta time.
		if self.can_move == False:
			if self.static_time <= 0:
				self.can_move=True
				self.static_time = 0
			else :
				self.change_x = 0
				self.change_y = 0
				self.static_time -= delta_time
		
		# Handle isSuperDrunk
		if self.BAC >= SUPER_DRUNK_LEVEL_PLAYER:
			if self.isSuperDrunk == False: self.isSuperDrunk = True
		else:
			self.isSuperDrunk = False

		# Decrease the invincible_time attribute by delta time.
		if self.invincible == True:
			if self.invincible_time <= 0:
				self.invincible=False
			else :
				self.invincible_time -= delta_time
