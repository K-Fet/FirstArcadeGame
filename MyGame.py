import random
import arcade
import os
from securitas import *
from player import *
 
SPRITE_SCALING_WALL= 0.1
SPRITE_SCALING_SECU= 0.05 
SPRITE_SCALING_PLAYER= 0.15
SPRITE_SCALING_BIER=0.1

BIER_COUNT=50
SECU_COUNT=8

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
OFFSCREEN_SPACE=0
LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE

MOVEMENT_SPEED=3

class MyGame(arcade.Window):

	def _init__(self):
		super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,"K-Fêt world")
		file_path=os.path.dirname(os.path.abspath(__file__))
		os.chdir(file_path)

		self.player_list=None
		self.bier_list=None
		self.secu_list=None
		self.wall_list=None
		self.all_sprites_list=None

		self.player_sprite=None
		self.score=0
		self.game_over=False

		self.set_mouse_visible(False)

		arcade.set_background_color(arcade.color.BLACK)

	def setup(self):
		self.player_list=arcade.SpriteList()
		self.bier_list=arcade.SpriteList()
		self.secu_list=arcade.SpriteList()
		self.wall_list=arcade.SpriteList()
		self.all_sprites_list=arcade.SpriteList()

		self.score=0
		self.game_over=False
		self.player_sprite=player(SPRITE_SCALING_PLAYER)
		self.player_sprite.center_x=50
		self.player_sprite.center_y=50
		self.player_list.append(self.player_sprite)
		self.all_sprites_list.append(self.player_sprite)

		for i in range(BIER_COUNT):
			bier=arcade.Sprite("Image/bier.png",SPRITE_SCALING_BIER)

			bier.center_x=random.randrange(SCREEN_WIDTH)
			bier.center_y=random.randrange(SCREEN_HEIGHT)

			self.bier_list.append(bier)
			self.all_sprites_list.append(bier)

		for j in range(SECU_COUNT):
			secu=securitas(SPRITE_SCALING_SECU)

			secu.center_x=random.randrange(SCREEN_WIDTH)
			secu.center_y=random.randrange(SCREEN_HEIGHT)

			secu.change_x=random.random()*2-1
			secu.change_y=random.random()*2-1

			#secu.change_angle=(random.random()-0.5)*2

			self.secu_list.append(secu)
			self.all_sprites_list.append(secu)

		for x in range(173, 650, 64):
			wall = arcade.Sprite("Image/wall.png", SPRITE_SCALING_WALL)
			wall.center_x = x
			wall.center_y = 200
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)

        # Create a column of boxes
		for y in range(273, 500, 64):
			wall = arcade.Sprite("Image/wall.png", SPRITE_SCALING_WALL)
			wall.center_x = 465
			wall.center_y = y
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
		self.physics_engine=arcade.PhysicsEngineSimple(self.player_sprite,self.wall_list)

	def on_draw(self):
		arcade.start_render()
		self.all_sprites_list.draw()
		self.wall_list.draw()

		output=f"Score: {self.score}"
		arcade.draw_text(output,10,20,arcade.color.RED,14)

	def on_key_press(self, key, modifiers):

		if key == arcade.key.UP:
			self.player_sprite.change_y=MOVEMENT_SPEED
		if key == arcade.key.DOWN:
			self.player_sprite.change_y=(-MOVEMENT_SPEED)
		if key == arcade.key.LEFT:
			self.player_sprite.change_x=(-MOVEMENT_SPEED)
		if key == arcade.key.RIGHT:
			self.player_sprite.change_x=MOVEMENT_SPEED
			print(self.player_sprite.change_x)

	def on_key_release(self, key, modifiers):

		if key == arcade.key.UP or key == arcade.key.DOWN:
			self.player_sprite.change_y = 0
		if key == arcade.key.LEFT or key == arcade.key.RIGHT:
			self.player_sprite.change_x = 0
			
##################### Souris ##################################
#	def on_mouse_motion(self,x,y,dx,dy):
#		for wall in self.wall_list :
#			if x == wall.center_x and y == wall.center_y:
#				print("Tentative de collision")
#			else:
#				self.player_sprite.center_x=x
#				self.player_sprite.center_y=y
###############################################################

	def update(self,delta_time):
		if not(self.game_over):
			self.all_sprites_list.update()
			self.physics_engine.update()
			bier_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.bier_list)
			secu_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.secu_list)

			for bier in bier_hit_list:
				bier.kill()
				self.score+=1

			if len(secu_hit_list)>0 :
				self.game_over=True
		else : 
			arcade.quick_run(0.25)

def main():
	window=MyGame()
	window.setup()
	arcade.run()

if __name__=="__main__":
	main()
			

