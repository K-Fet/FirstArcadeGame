import arcade 
import os
from data import *
from player import *
from beer import *
from securitas import *
from vomit import *
from map import *
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
    
    self.player = None
    
    # To be responsive
    self.screen_width,self.screen_height = self.get_size()

    # Sprites
    self.username="Bd"
    self.player = None
    
    self.beer_list= None

    self.securitas_sprite = None
    self.securitas_list = None

    self.vomit_list=None

    self.all_sprite_list = None

    # Windows 
    self.game_over = False
    self.menu = True
    self.highscore = False

    # Statics graphics elements organisation 
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
    
    # Background image will be stored in this variable
    self.background = None

    # Set the working directory (where we expect to find files) to the same
    # directory this .py file is in.
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)
  
  def setup(self):
    self.player = player(self.screen_width/2,self.screen_height/2)
    self.player.can_move=True

    # Sprite lists SETUP
    self.all_sprite_list=arcade.SpriteList()
    self.beer_list=arcade.SpriteList()
    self.vomit_list=arcade.SpriteList()

    self.background = arcade.load_texture("img/map1_1280.png")

    beer_sprite=beer(self.screen_width//2, self.screen_height//2)
    self.beer_list.append(beer_sprite)
    
    self.score=0
    self.player.BAC=0
    self.total_time=0

    self.map = Map("maps/map1.csv")

    self.physic_engines_list = list()

    self.physic_engines_list.append(arcade.PhysicsEngineSimple(self.player,self.map.wall_list))

    # Secu
    securitas_1 = securitas(self.screen_width // 2 + 250,self.screen_height // 2 - 100)
    securitas_2 = securitas(self.screen_width // 2 - 250,self.screen_height // 2 + 250)
    self.securitas_list=arcade.SpriteList()

    self.securitas_list.append(securitas_1)
    self.securitas_list.append(securitas_2)

    self.all_sprite_list.append(securitas_1)
    self.all_sprite_list.append(securitas_2)

    # Physic engines setup
    self.physic_engines_list.append(arcade.PhysicsEngineSimple(securitas_1,self.map.wall_list))
    self.physic_engines_list.append(arcade.PhysicsEngineSimple(securitas_2,self.map.wall_list))

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
      # Background
      arcade.draw_texture_rectangle(self.screen_width // 2, self.screen_height // 2,
                                      self.screen_width, self.screen_height, self.background)

      self.beer_list.draw()
      self.vomit_list.draw()
      self.all_sprite_list.draw()
      self.player.draw()
      self.map.wall_list.draw()

      minutes=int(self.total_time)//60
      seconds=int(self.total_time)%60
  
      output_score=f"Score: {int(self.score)}"
      output_time=f"Time: {minutes:02d}:{seconds:02d}"
      arcade.draw_text(output_score,10,20,arcade.color.RED,14)
      arcade.draw_text(output_time,10,50,arcade.color.RED,14)

  def update(self, delta_time):
    if (self.game_over == False and self.menu==False and self.highscore==False):
      self.beer_list.update()

      for vomit_sprites in self.vomit_list : 
        vomit_sprites.life-=delta_time
        if vomit_sprites.life<0:
          vomit_sprites.kill()

      # Manual updates

      self.player.update(delta_time)
      for securitas in self.securitas_list:
        securitas.update(delta_time)

      # PHYSIC ENGINE UPDATE
      for physics_engine in self.physic_engines_list:
        physics_engine.update()

      self.total_time+=delta_time

      securitas_hit_list = arcade.check_for_collision_with_list(self.player,self.securitas_list)
      beer_hit_list = arcade.check_for_collision_with_list(self.player,self.beer_list)
      vomit_hit_list = arcade.check_for_collision_with_list(self.player,self.vomit_list)
      
      for securitas_sprite in self.securitas_list:
        secu_vomit_hit_list = arcade.check_for_collision_with_list(securitas_sprite,self.vomit_list)
        secu_beer_hit_list = arcade.check_for_collision_with_list(securitas_sprite,self.beer_list)
        if len(secu_vomit_hit_list)>0:
          securitas_sprite.static_time=TIME_STATIC
          securitas_sprite.can_move=False
          securitas_sprite.change_x=0
          securitas_sprite.change_y=0
        for vomit_sprites in secu_vomit_hit_list:
          vomit_sprites.kill()
        for beer_sprites in secu_beer_hit_list:
          beer_sprites.kill()
          securitas_sprite.BAC+=1
          new_beer_sprite=beer()
          self.beer_list.append(new_beer_sprite)
      
      # generate new beer if collision with player
      if len(beer_hit_list) > 0: 
        new_beer = beer()
        self.beer_list.append(new_beer)
      
      # ???? More beers ?
      if self.player.BAC>5 and len(self.beer_list) < 10:
          beer_sprite=beer()
          self.beer_list.append(beer_sprite)

      for beer_sprite_hit in beer_hit_list:
        print("BEER KILL")
        beer_sprite_hit.kill()
        self.player.BAC+=1
        
     
      if len(vomit_hit_list)>0:
        self.player.can_move=False
        self.player.static_time=TIME_STATIC

      if len(securitas_hit_list)>0 :
        self.game_over=True   
        self.score=self.score*self.total_time

        highscore=take_scores()
        if len(highscore)<10:
          while self.username in highscore:
            self.username+="@"
          highscore[self.username]=int(self.score)
          save_score(highscore)
        else:
          if self.score>highscore[min(highscore,key=highscore.get)]:
            del highscore[min(highscore,key=highscore.get)]
            while self.player.username in highscore:
              self.player.username+="@"
            highscore[self.username]=int(self.score)
            save_score(highscore)

  def on_key_press(self, key, modifiers):
    if(self.game_over==False, self.menu==False, self.highscore==False):
      if(self.player.can_move):
        if key == arcade.key.UP:
          self.player.change_y = MOVEMENT_SPEED
        if key == arcade.key.DOWN:
          self.player.change_y = -MOVEMENT_SPEED
        if key == arcade.key.LEFT:
          self.player.change_x = -MOVEMENT_SPEED
        if key == arcade.key.RIGHT:
          self.player.change_x = MOVEMENT_SPEED



  def on_key_release(self, key, modifiers):
    if(self.game_over==False, self.menu==False, self.highscore==False):
      if key == arcade.key.UP or key == arcade.key.DOWN:
        self.player.change_y = 0
      if key == arcade.key.LEFT or key == arcade.key.RIGHT:
        self.player.change_x = 0
      if key == arcade.key.TAB and self.player.BAC>0:
          self.score+=self.player.BAC
          self.player.BAC=0
          vomit_sprite=vomit(self.player.center_x+self.player.change_x*10,self.player.center_y+self.player.change_y*10)
          self.vomit_list.append(vomit_sprite)

          
          
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
