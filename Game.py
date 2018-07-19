import arcade 
from data import *
from player import *

class Game(arcade.Window):

  def __init__(self,screen_width=SCREEN_WIDTH,screen_height=SCREEN_HEIGHT):
    super().__init__(screen_width, screen_height, fullscreen=True)
    arcade.set_background_color(arcade.color.AMAZON)
    self.player = None
    self.screen_width,self.screen_height = self.get_size()
  
    self.beer_sprite=None
    self.beer_list=None

    self.securitas_sprite=None
    self.securitas_list=None

    self.all_sprite_list=None

  
  def setup(self):
    self.player = player(self.screen_width/2,self.screen_height/2)
    self.all_sprite_list=arcade.SpriteList()

    self.beer_list=arcade.SpriteList()
    self.beer=beer(50,50)
    self.beer_list.append(self.beer)

    self.securitas_list=arcade.SpriteList()
    self.securitas=securitas(100,100)
    self.securitas_list.append(self.securitas)
    self.all_sprite_list.append(self.securitas)
    pass

  def update(self, delta_time):
    self.all_sprite_list.update()
    self.beer_list.update()
    self.player.update(self.screen_width, self.screen_height)

  def on_draw(self): 
    arcade.start_render()
    self.player.draw()
    

  def on_key_press(self, key, modifiers):
    if key == arcade.key.UP:
      self.player.change_y = MOVEMENT_SPEED
    if key == arcade.key.DOWN:
      self.player.change_y = -MOVEMENT_SPEED
    if key == arcade.key.LEFT:
      self.player.change_x = -MOVEMENT_SPEED
    if key == arcade.key.RIGHT:
      self.player.change_x = MOVEMENT_SPEED

  def on_key_release(self, key, modifiers):
    if key == arcade.key.UP or key == arcade.key.DOWN:
      self.player.change_y = 0
    if key == arcade.key.LEFT or key == arcade.key.RIGHT:
      self.player.change_x = 0
    
def main():

    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
  main()
