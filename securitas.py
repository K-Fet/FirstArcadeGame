import arcade
from data import *
import random

class securitas(arcade.Sprite):
	def __init__(self,center_x,center_y):
		super().__init__("img/securitas.png",SPRITE_SCALING_SECURITAS)
		self.center_x=center_x
		self.center_y=center_y

		
		securitas_initial_direction=random.randrange(1,5,1)
		if(securitas_initial_direction==RIGHT):
			self.change_x=SECURITAS_SPEED
		elif(securitas_initial_direction==LEFT):
			self.change_x=(-SECURITAS_SPEED)
		elif(securitas_initial_direction==UP):
			self.change_y=SECURITAS_SPEED	
		else :
			self.change_y=(-SECURITAS_SPEED)
	def update(self,screen_width,screen_heigth,keys_disable=[False,False,False,False]):
		super().update()	

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

		if keys_disable[0] : self.change_x = -abs(self.change_x) 
		if keys_disable[1] : self.change_x = abs(self.change_x)
		if keys_disable[2] : self.change_y = -abs(self.change_y) 
		if keys_disable[3] : self.change_y = abs(self.change_y)
		
		if self.center_x < BORDERS_OFFSET :
			if self.change_x < 0 or keys_disable[0] : self.change_x = -self.change_x
		if self.center_x > screen_width - BORDERS_OFFSET:
			if self.change_x > 0 or keys_disable[1] : self.change_x = -self.change_x
		if self.center_y < BORDERS_OFFSET:
			if self.change_y < 0 or keys_disable[2]: self.change_y = -self.change_y
		if self.center_y > screen_heigth - BORDERS_OFFSET:
			if self.change_y > 0  or keys_disable[3]: self.change_y = -self.change_y

