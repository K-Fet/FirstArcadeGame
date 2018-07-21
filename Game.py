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
  
    if os.path.exists(HIGHSCORE_FILE) and os.path.getsize(HIGHSCORE_FILE) > 0: # File exists
        highscore_file = open(HIGHSCORE_FILE, "rb")
        mon_depickler = pickle.Unpickler(highscore_file)
        scores = mon_depickler.load()
        highscore_file.close()
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

    self.line_break=screen_height/5

    self.play_position_x=self.screen_width / 2
    self.play_position_y=(3/4)*self.screen_height
    self.play_height=self.screen_height/14
    self.play_width=int(4*0.4*self.play_height) #Nb_lettre*largeur_lettre

    self.menu_highscore_position_x=self.screen_width / 2
    self.menu_highscore_position_y=(3/4)*self.screen_height - self.play_height - self.line_break
    self.menu_highscore_height=self.screen_height/14
    self.menu_highscore_width=int(10*0.4*self.menu_highscore_height)

    self.quit_position_x=self.screen_width / 2
    self.quit_position_y=(3/4)*self.screen_height - self.play_height - self.menu_highscore_height - 2*self.line_break
    self.quit_height=self.screen_height/14
    self.quit_width=int(4*0.4*self.quit_height)

    self.game_over_position_x=self.screen_width / 2
    self.game_over_height=self.screen_height/10
    self.game_over_position_y=(self.screen_height / 2) + self.game_over_height

    self.backmenu_position_x=(self.screen_width)*(1/10)
    self.backmenu_position_y=(self.screen_height)*(1/10)
    self.backmenu_height=self.screen_height/20
    self.backmenu_width=int(10*0.4*self.backmenu_height)

    self.backhighscore_position_x=(self.screen_width)*(9/10)
    self.backhighscore_position_y=(self.screen_height)*(1/10)
    self.backhighscore_height=self.screen_height/20
    self.backhighscore_width=int(10*0.4*self.backhighscore_height)

    self.restart_position_x=self.screen_width / 2
    self.restart_position_y=(self.screen_height / 2) - self.game_over_height
    self.restart_height=self.screen_height/20
    self.restart_width=int(10*0.4*self.restart_height)

    self.highscore_position_x=self.screen_width / 2
    self.highscore_position_y=self.screen_height - self.line_break/4
    self.highscore_height=54
    self.highscore_width=int(10*0.4*self.highscore_height)
  
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
      arcade.draw_text(output, self.game_over_position_x, self.game_over_position_y, arcade.color.WHITE, self.game_over_height, align="center",anchor_x="center",anchor_y="center")

      output = "Click to restart"
      arcade.draw_text(output, self.restart_position_x, self.restart_position_y, arcade.color.WHITE, self.restart_height, align="center",anchor_x="center",anchor_y="center")

      output = "menu"
      arcade.draw_text(output,self.backmenu_position_x, self.backmenu_position_y, arcade.color.WHITE, self.backmenu_height,align="center",anchor_x="center",anchor_y="center")

      output = "high score"
      arcade.draw_text(output,self.backhighscore_position_x, self.backhighscore_position_y, arcade.color.WHITE, self.backhighscore_height,align="center",anchor_x="center",anchor_y="center")

    elif (self.menu):
      output = "Play"
      arcade.draw_text(output, self.play_position_x, self.play_position_y, arcade.color.WHITE, self.play_height,align="center",anchor_x="center",anchor_y="center")

      output = "High Score"
      arcade.draw_text(output, self.menu_highscore_position_x, self.menu_highscore_position_y, arcade.color.WHITE, self.menu_highscore_height,align="center",anchor_x="center",anchor_y="center")

      output = "Quit"
      arcade.draw_text(output, self.quit_position_x, self.quit_position_y, arcade.color.WHITE, self.quit_height,align="center",anchor_x="center",anchor_y="center")

    elif (self.highscore):
      output = "High Score"
      arcade.draw_text(output, self.highscore_position_x, self.highscore_position_y,arcade.color.WHITE, self.highscore_height,align="center",anchor_x="center",anchor_y="center")
      list_highscore=take_scores()
      rank=1
      
      sorted_highscore=sorted(list_highscore.items(),key=operator.itemgetter(1),reverse=True)

      for pair in sorted_highscore :
        keys=re.sub('@','',pair[0])
        output=str(rank)+ " : " + keys + "  "+ str(pair[1])# + keys 
        arcade.draw_text(output, self.highscore_position_x, self.highscore_position_y - self.highscore_height*rank - self.line_break*(rank+2)/15,arcade.color.WHITE,align="center",anchor_x="center",anchor_y="center")
        rank+=1

      output = "menu"
      arcade.draw_text(output,self.backmenu_position_x, self.backmenu_position_y, arcade.color.WHITE, self.backmenu_height,align="center",anchor_x="center",anchor_y="center")

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

        highscore=take_scores()
        print(len(highscore))
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
      if x < self.restart_position_x + self.restart_width and x > self.restart_position_x - self.restart_width and y < self.restart_position_y + self.restart_height and y > self.restart_position_y - self.restart_height :
        self.setup()
        self.game_over=False
      elif x < self.backmenu_position_x + self.backmenu_width and x > self.backmenu_position_x - self.backmenu_width and y < self.backmenu_position_y + self.backmenu_height and y > self.backmenu_position_y - self.backmenu_height :
         self.game_over=False
         self.menu=True
      elif x < self.backhighscore_position_x + self.backhighscore_width and x > self.backhighscore_position_x - self.backhighscore_width and y < self.backhighscore_position_y + self.backhighscore_height and y > self.backhighscore_position_y - self.backhighscore_height :
         self.game_over=False
         self.highscore=True
    elif self.menu:
      if x < self.play_position_x + self.play_width and x > self.play_position_x - self.play_width and y < self.play_position_y + self.play_height and y > self.play_position_y - self.play_height :
        self.setup()
        self.menu=False
      elif  x < self.menu_highscore_position_x + self.menu_highscore_width and x > self.menu_highscore_position_x - self.menu_highscore_width and y < self.menu_highscore_position_y + self.menu_highscore_height and y > self.menu_highscore_position_y - self.menu_highscore_height :
        self.menu=False
        self.highscore=True
      elif  x < self.quit_position_x + self.quit_width and x > self.quit_position_x - self.quit_width and y < self.quit_position_y + self.quit_height and y > self.quit_position_y - self.quit_height :
        arcade.quick_run(0.5)
    elif self.highscore :
      if x < self.backmenu_position_x + self.backmenu_width and x > self.backmenu_position_x - self.backmenu_width and y < self.backmenu_position_y + self.backmenu_height and y > self.backmenu_position_y - self.backmenu_height :
        self.highscore=False
        self.menu=True
       

def main():
    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
  main()
