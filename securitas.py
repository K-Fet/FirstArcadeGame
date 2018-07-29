import arcade
from data import *
import random

class securitas(arcade.Sprite):
	def __init__(self,filename,center_x,center_y,isAngry=False):
		super().__init__(filename,SPRITE_SCALING_SECURITAS)
		
		# Initial position
		self.center_x=center_x
		self.center_y=center_y

		# Securitas SETUP
		self.can_move=True
		self.isAngry = isAngry
		self.static_time=0
		self.BAC=0
		self.prev_x = None
		self.prev_y = None
		self.player_around = False
		
		# First movement SETUP
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
		# update prev x y and y
		self.prev_x = self.center_x
		self.prev_y = self.center_y

		# The securitas can move
		if self.can_move==True:
			securitas_change=random.randrange(1,30,1)
			if(securitas_change==1):
				securitas_new_direction=random.randrange(1,5,1)
				if(securitas_new_direction==RIGHT):
					self.change_x = (SECURITAS_SPEED if self.isAngry == False else ANGRY_SECURITAS_SPEED)
				elif(securitas_new_direction==LEFT):
					self.change_x = (-SECURITAS_SPEED if self.isAngry == False else -ANGRY_SECURITAS_SPEED)
				elif(securitas_new_direction==UP):
					self.change_y = (SECURITAS_SPEED	if self.isAngry == False else ANGRY_SECURITAS_SPEED)
				else :
					self.change_y= (-SECURITAS_SPEED if self.isAngry == False else -ANGRY_SECURITAS_SPEED)
 
		

		# The securitas walked into a vomit and he is blocked
		if self.static_time<0:
			self.can_move=True
		else:
			self.static_time-=delta_time

	def check_for_physic_engine_block(self):
		if self.prev_x == self.center_x and self.prev_y == self.center_y : 
			self.change_x = -self.change_x
			self.change_y = -self.change_y
		
	def check_if_player_around(self, player):
		dist = arcade.sprite.get_distance_between_sprites(self, player)
		self.player_around = True if (dist <= SECURITAS_RADIUS) else False

	def check_if_charge_player(self, player):
		if self.isAngry and self.player_around:
			dist_x = self.center_x - player.center_x
			dist_y = self.center_y - player.center_y
			if abs(dist_x) <= ANGRY_SECURITAS_SPEED:
				self.center_x = player.center_x
			else:
				self.change_x = ANGRY_SECURITAS_SPEED	 if dist_x < 0 else -ANGRY_SECURITAS_SPEED
			if abs(dist_y) <= ANGRY_SECURITAS_SPEED:
				self.center_y = player.center_y
			else:
				self.change_y = ANGRY_SECURITAS_SPEED if dist_y < 0 else -ANGRY_SECURITAS_SPEED

