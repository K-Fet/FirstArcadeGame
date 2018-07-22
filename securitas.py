import arcade
from data import *
import random

class securitas(arcade.Sprite):
	def __init__(self,center_x,center_y):
		super().__init__("img/securitas.png",SPRITE_SCALING_SECURITAS)
		self.center_x=center_x
		self.center_y=center_y
		self.can_move=True
		self.static_time=0
		self.BAC=0
		
		securitas_initial_direction=random.randrange(1,5,1)
		if(securitas_initial_direction==RIGHT):
			self.change_x=SECURITAS_SPEED
		elif(securitas_initial_direction==LEFT):
			self.change_x=(-SECURITAS_SPEED)
		elif(securitas_initial_direction==UP):
			self.change_y=SECURITAS_SPEED	
		else :
			self.change_y=(-SECURITAS_SPEED)

	def update(self,delta_time):
		if self.can_move==True:
			securitas_change=random.randrange(1,30,1)
			if(securitas_change==1):
				securitas_new_direction=random.randrange(1,5,1)
				if(securitas_new_direction==RIGHT):
					self.change_x=SECURITAS_SPEED
				elif(securitas_new_direction==LEFT):
					self.change_x=(-SECURITAS_SPEED)
				elif(securitas_new_direction==UP):
					self.change_y=SECURITAS_SPEED	
				else :
					self.change_y=(-SECURITAS_SPEED)



			if self.static_time<0:
				self.can_move=True
			else:
				self.static_time-=delta_time
