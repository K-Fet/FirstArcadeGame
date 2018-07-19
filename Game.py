import arcade 
from data import *
from player import *

class Game(arcade.Window):

  def __init__(self,screen_width=SCREEN_WIDTH,screen_height=SCREEN_HEIGHT):
    super().__init__(screen_width, screen_height, fullscreen=True)
    arcade.set_background_color(arcade.color.AMAZON)
    self.player = None

    width, heigth = self.get_size()
    self.set_viewport(0, width, 0, heigth)

  
  
  def setup(self):
    self.player = player(0,0)

  def on_draw(self): 
    arcade.start_render()
    self.player.draw()

  def update(self, delta_time):
    self.player.update()

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
    elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
      self.player.change_x = 0

    
def main():

    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
  main()
