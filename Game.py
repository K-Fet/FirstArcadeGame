import arcade 
from data import *

class Game(arcade.Window):

  def __init__(self,screen_width=SCREEN_WIDTH,screen_height=SCREEN_HEIGHT):
    super().__init__(screen_width, screen_height)
    arcade.set_background_color(arcade.color.AMAZON)
  
    self.beer_sprite=None
    self.beer_list=None

    self.securitas_sprite=None
    self.securitas_list=None

    self.all_sprite_list=None

  
  def setup(self):
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
    pass
  
  

def main():

    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
  main()
