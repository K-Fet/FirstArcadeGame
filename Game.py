import arcade 
from data import *

class Game(arcade.Window):

  def __init__(self,screen_width=SCREEN_WIDTH,screen_height=SCREEN_HEIGHT):
    super().__init__(screen_width, screen_height)
    arcade.set_background_color(arcade.color.BLACK)
  
  
  def setup(self):

    pass

  def update(self, delta_time):

    pass

def main():

    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
  main()
