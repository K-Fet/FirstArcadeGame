import random
import arcade
import os
from securitas import *
from player import *
from data import *
from bier import *

class MyGame(arcade.Window):
	def _init__(self):
		super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,"K-Fêt world")
		# file_path=os.path.dirname(os.path.abspath(__file__))
		# os.chdir(file_path)

		self.player_list=None
		self.bier_list=None
		self.secu_list=None
		self.wall_list=None
		self.all_sprites_list=None

		self.player_sprite=None
		self.score=0
		self.game_over=False
		self.total_time=TOTAL_TIME

		self.set_mouse_visible(False)

		arcade.set_background_color(arcade.color.BLACK)

	def setup(self):
		self.player_list=arcade.SpriteList()
		self.bier_list=arcade.SpriteList()
		self.secu_list=arcade.SpriteList()
		self.wall_list=arcade.SpriteList()
		self.all_sprites_list=arcade.SpriteList()

		self.total_time=TOTAL_TIME	
		self.score=0
		self.game_over=False
		
		self.player_sprite=player()
		self.player_list.append(self.player_sprite)
		self.all_sprites_list.append(self.player_sprite)

		for i in range(BIER_COUNT):
			self.bier=bier()

			self.bier_list.append(self.bier)

		for j in range(SECU_COUNT):
			self.secu=securitas()

			self.secu_list.append(self.secu)
			self.all_sprites_list.append(self.secu)

		for x in range(173, 650, 32):
			wall = arcade.Sprite("Image/wall.png", SPRITE_SCALING_WALL)
			wall.center_x = x
			wall.center_y = 200
			self.wall_list.append(wall)

        # Create a column of boxes
		for y in range(273, 500, 32):
			wall = arcade.Sprite("Image/wall.png", SPRITE_SCALING_WALL)
			wall.center_x = 465
			wall.center_y = y
			self.wall_list.append(wall)
		self.physics_engine=arcade.PhysicsEngineSimple(self.player_sprite,self.wall_list)
	""" Don't put static object in all_sprites because there will update with dynamics objects """
	def on_draw(self):
		arcade.start_render()
		self.all_sprites_list.draw()
		self.wall_list.draw()
		self.bier_list.draw()

		minutes=int(self.total_time)//60
		seconds=int(self.total_time)%60

		output_score=f"Score: {self.score} "
		output_time=f"Time: {minutes:02d}:{seconds:02d}"
		arcade.draw_text(output_score,10,20,arcade.color.RED,14)
		arcade.draw_text(output_time,700,20,arcade.color.RED,14)

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
		if int(self.total_time)==0:
			self.game_over=True
		if not(self.game_over):
			self.total_time-=delta_time
			
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
			

