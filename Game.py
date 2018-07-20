import arcade 
from data import *
from player import *
from stripline import *

class Game(arcade.Window):

  def __init__(self,screen_width=SCREEN_WIDTH,screen_height=SCREEN_HEIGHT):
    super().__init__(screen_width, screen_height, fullscreen=FULLSCREEN)
    arcade.set_background_color(arcade.color.AMAZON)
    self.player = None
    self.screen_width,self.screen_height = self.get_size()
  
  
  def setup(self):
    linepoints = ((0,0),(self.screen_width/2, self.screen_height/2))
    self.stripline = stripline(linepoints)
    self.player = player(self.screen_width/2,self.screen_height/2)

  def on_draw(self): 
    arcade.start_render()
    self.stripline.draw()
    self.player.draw()

  def update(self, delta_time):
    self.player.update(self.screen_width, self.screen_height)
    

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
