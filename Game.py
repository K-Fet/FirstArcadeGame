import arcade 
from data import *
from player import *
from stripline import *
from beer import *
from securitas import *

class Game(arcade.Window):

  def __init__(self,screen_width=SCREEN_WIDTH,screen_height=SCREEN_HEIGHT):
    super().__init__(screen_width, screen_height, fullscreen=FULLSCREEN)
    arcade.set_background_color(arcade.color.AMAZON)
    self.player = None
    self.screen_width,self.screen_height = self.get_size()
  
    self.beer_sprite=None
    self.beer_list=None

    self.securitas_sprite=None
    self.securitas_list=None

    self.all_sprite_list=None

    self.game_over=False

  
  def setup(self):
    linepoints = ((0,0),(self.screen_width/2, self.screen_height/2))
    self.stripline = stripline(linepoints)
    self.player = player(self.screen_width/2,self.screen_height/2)
    self.all_sprite_list=arcade.SpriteList()

    self.beer_list=arcade.SpriteList()
    self.beer=beer()
    self.beer_list.append(self.beer)

    self.securitas_list=arcade.SpriteList()
    self.securitas=securitas(1070,110)
    self.securitas_list.append(self.securitas)
    self.all_sprite_list.append(self.securitas)
    self.securitas=securitas(220,675)
    self.securitas_list.append(self.securitas)
    self.all_sprite_list.append(self.securitas)
    
    self.score=0
    self.total_time=0
    pass


  def on_draw(self): 
    arcade.start_render()
    self.stripline.draw()
    self.beer_list.draw()
    self.all_sprite_list.draw()
    self.player.draw()

    minutes=int(self.total_time)//60
    seconds=int(self.total_time)%60
  
    output_score=f"Score: {self.score} "
    output_time=f"Time: {minutes:02d}:{seconds:02d}"
    arcade.draw_text(output_score,10,20,arcade.color.RED,14)
    arcade.draw_text(output_time,10,50,arcade.color.RED,14)


  def update(self, delta_time):

    if not(self.game_over):
      self.all_sprite_list.update()
      self.beer_list.update()
      self.player.update(self.screen_width, self.screen_height)  

      self.total_time+=delta_time

      securitas_hit_list = arcade.check_for_collision_with_list(self.player,self.securitas_list)
      beer_hit_list = arcade.check_for_collision_with_list(self.player,self.beer_list)

      for beer in beer_hit_list:
        beer.kill()
        self.score+=1
      if len(securitas_hit_list)>0 :
        self.game_over=True
    else : 
      arcade.quick_run(0.25)


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
