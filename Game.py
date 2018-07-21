import arcade 
from data import *
from player import *
from stripline import *
from beer import *
from securitas import *
import os
import pickle
import re
import operator


def take_scores():
    scores={}   
    if os.path.exists(HIGHSCORE_FILE) and os.path.getsize(HIGHSCORE_FILE) > 0: # File exists
        highscore = open(HIGHSCORE_FILE, "rb")
        mon_depickler = pickle.Unpickler(highscore)
        scores = mon_depickler.load()
        highscore.close()
    else: # File does not exist
        scores = {}
    return scores

def save_score(scores):
  highscore = open(HIGHSCORE_FILE, "wb") # On écrase les anciens scores
  mon_pickler = pickle.Pickler(highscore)
  mon_pickler.dump(scores)
  highscore.close()

class Game(arcade.Window):

  def __init__(self,screen_width=SCREEN_WIDTH,screen_height=SCREEN_HEIGHT):
    super().__init__(screen_width, screen_height, fullscreen=FULLSCREEN)
    arcade.set_background_color(arcade.color.AMAZON)

    self.username="Lucas"
    self.player = None
    self.screen_width,self.screen_height = self.get_size()
  
    self.beer_list=None

    self.securitas_sprite=None
    self.securitas_list=None

    self.all_sprite_list=None

    self.game_over=False
    self.menu=True
    self.highscore=False

  
  def setup(self):
    linepoints = ((0,0),(self.screen_width/2, self.screen_height/2))
    self.stripline = stripline(linepoints)
    self.player = player(self.screen_width/2,self.screen_height/2)
    self.all_sprite_list=arcade.SpriteList()

    self.beer_list=arcade.SpriteList()

    beer_sprite=beer()
    self.beer_list.append(beer_sprite)

    self.securitas_list=arcade.SpriteList()
    self.securitas=securitas(1070,110)
    self.securitas_list.append(self.securitas)
    self.all_sprite_list.append(self.securitas)
    self.securitas=securitas(220,675)
    self.securitas_list.append(self.securitas)
    self.all_sprite_list.append(self.securitas)
    
    self.score=0
    self.total_time=0
    


  def on_draw(self): 
    arcade.start_render()
    if self.game_over :
       
      score=self.score*self.total_time

      output = f"Game Over - Score : {int(self.score)}"
      arcade.draw_text(output, GAME_OVER_POSITION_X, GAME_OVER_POSITION_Y, arcade.color.WHITE, GAME_OVER_HEIGHT, align="center",anchor_x="center",anchor_y="center")

      output = "Click to restart"
      arcade.draw_text(output, RESTART_POSITION_X, RESTART_POSITION_Y, arcade.color.WHITE, RESTART_HEIGHT, align="center",anchor_x="center",anchor_y="center")
    
    elif (self.menu):
      output = "Play"
      arcade.draw_text(output, PLAY_POSITION_X, PLAY_POSITION_Y, arcade.color.WHITE, PLAY_HEIGHT,align="center",anchor_x="center",anchor_y="center")

      output = "High Score"
      arcade.draw_text(output, MENU_HIGHSCORE_POSITION_X, MENU_HIGHSCORE_POSITION_Y, arcade.color.WHITE, MENU_HIGHSCORE_HEIGHT,align="center",anchor_x="center",anchor_y="center")

      output = "Quit"
      arcade.draw_text(output, QUIT_POSITION_X, QUIT_POSITION_Y, arcade.color.WHITE, QUIT_HEIGHT,align="center",anchor_x="center",anchor_y="center")

    elif (self.highscore):
      output = "High Score"
      arcade.draw_text(output, HIGHSCORE_POSITION_X, HIGHSCORE_POSITION_Y,arcade.color.WHITE, HIGHSCORE_HEIGHT,align="center",anchor_x="center",anchor_y="center")
      highscore=take_scores()
      rank=1
      
      sorted_highscore=sorted(highscore.items(),key=operator.itemgetter(1),reverse=True)

      for pair in sorted_highscore :
        keys=re.sub('@','',pair[0])
        output=str(rank)+ " : " + keys + "  "+ str(pair[1])# + keys 
        arcade.draw_text(output, HIGHSCORE_POSITION_X, HIGHSCORE_POSITION_Y - HIGHSCORE_HEIGHT*rank - LINE_BREAK*rank/6,arcade.color.WHITE,align="center",anchor_x="center",anchor_y="center")
        rank+=1

    else:
      self.stripline.draw()
      self.beer_list.draw()
      self.all_sprite_list.draw()
      self.player.draw()

      minutes=int(self.total_time)//60
      seconds=int(self.total_time)%60
  
      output_score=f"Score: {int(self.score)}"
      output_time=f"Time: {minutes:02d}:{seconds:02d}"
      arcade.draw_text(output_score,10,20,arcade.color.RED,14)
      arcade.draw_text(output_time,10,50,arcade.color.RED,14)

  def update(self, delta_time):
    if (self.game_over == False and self.menu==False and self.highscore==False):
      self.beer_list.update()
      self.disabledKeys = self.stripline.check_for_collisions_with_player(self.player.center_x, self.player.center_y) 
    
      self.player.update(self.screen_width, self.screen_height, self.disabledKeys)
      for securitas_sprite in self.securitas_list:
        securitas_disableKeys=self.stripline.check_for_collisions_with_player(securitas_sprite.center_x,securitas_sprite.center_y)
        securitas_sprite.update(self.screen_width, self.screen_height,securitas_disableKeys)

       
      self.total_time+=delta_time

      securitas_hit_list = arcade.check_for_collision_with_list(self.player,self.securitas_list)
      beer_hit_list = arcade.check_for_collision_with_list(self.player,self.beer_list)
      for x in range(len(beer_hit_list)):
        beer_sprite=beer()
        self.beer_list.append(beer_sprite)
      for beer_sprite_hit in beer_hit_list:
        beer_sprite_hit.kill()
        self.score+=1
        if self.score%3==0 and self.score<BEER_CONVERGENCE:
          beer_sprite=beer()
          self.beer_list.append(beer_sprite)
      if len(securitas_hit_list)>0 :
        
        self.game_over=True   
        self.score=self.score*self.total_time
        print(self.score)

        highscore=take_scores()

        if len(highscore)<10:
          while self.username in highscore:
            self.username+="@"
          highscore[self.username]=int(self.score)
          save_score(highscore)
          isNewHighscore=True
        else:
          if self.score>highscore[min(highscore,key=highscore.get)]:
            del highscore[min(highscore,key=highscore.get)]
          while self.username in highscore:
            self.username+="@"
          highscore[self.username]=int(self.score)
          save_score(highscore)


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
      
  def on_mouse_press(self,x,y,button,modifiers):
    if self.game_over :
      self.setup()
      self.game_over=False
    elif self.menu:
      if x < PLAY_POSITION_X + PLAY_WIDTH and x > PLAY_POSITION_X - PLAY_WIDTH and y < PLAY_POSITION_Y + PLAY_HEIGHT and y > PLAY_POSITION_Y - PLAY_HEIGHT :
        self.setup()
        self.menu=False
      elif  x < MENU_HIGHSCORE_POSITION_X + MENU_HIGHSCORE_WIDTH and x > MENU_HIGHSCORE_POSITION_X - MENU_HIGHSCORE_WIDTH and y < MENU_HIGHSCORE_POSITION_Y + MENU_HIGHSCORE_HEIGHT and y > MENU_HIGHSCORE_POSITION_Y - MENU_HIGHSCORE_HEIGHT :
        self.menu=False
        self.highscore=True
      elif  x < QUIT_POSITION_X + QUIT_WIDTH and x > QUIT_POSITION_X - QUIT_WIDTH and y < QUIT_POSITION_Y + QUIT_HEIGHT and y > QUIT_POSITION_Y - QUIT_HEIGHT :
        arcade.quick_run(0.5)
       

def main():
    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
  main()
