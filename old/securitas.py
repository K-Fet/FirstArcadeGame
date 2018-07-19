import arcade
from MyGame import *
from data import *

class securitas(arcade.Sprite):
	def __init__(self):
		super().__init__("Image/secu.png",SPRITE_SCALING_SECU)
		self.center_x=random.randrange(SCREEN_WIDTH)
		self.center_y=random.randrange(SCREEN_HEIGHT)

		self.change_x=random.random()*2-1
		self.change_y=random.random()*2-1
#secu.change_angle=(random.random()-0.5)*2
#	def setup(self):
#		self.physics_engine=arcade.PhysicsEngineSimple(self.player_sprite,self.wall_list)
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


