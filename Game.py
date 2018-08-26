import arcade 
import os
from data import *
from player import *
from beer import *
from securitas import *
from vomit import *
from map import *
from menu import *
from menus_items import *
import os
import pickle
import re
import operator

# Function which allow to recover highscores saved
def take_scores():
  
    if os.path.exists(HIGHSCORE_FILE) and os.path.getsize(HIGHSCORE_FILE) > 0: # File exists
        highscore_file = open(HIGHSCORE_FILE, "rb")
        mon_depickler = pickle.Unpickler(highscore_file)
        scores = mon_depickler.load()
        highscore_file.close()
    else: # File does not exist
        scores = {}
    return scores

# Function which allow to save highscores updated
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
    self.username="Coco & BD"
    self.player = None   # player object

    self.beer_list= None # list of beers objects

    self.current_beer_number = None

    self.securitas_list = None # list of securistas objects

    self.vomit_list=None # list of vomits object

    # Windows 
    self.game_over = False
    self.game_over_isHighscore=False
    self.menu = True
    self.highscores = False

    #Sounds 
    self.sounds_effects_list = None

    # Menu creation
    self.main_menu = Menu(MAIN_MENU[0], MAIN_MENU[1], self.screen_width, self.screen_height)
    self.high_scores_menu = Menu(HIGHSCORES_MENU[0], HIGHSCORES_MENU[1], self.screen_width, self.screen_height)
    self.high_score_menu = Menu(HIGHSCORE_MENU[0], HIGHSCORE_MENU[1], self.screen_width, self.screen_height)
    self.game_over_menu = Menu(GAME_OVER_MENU[0], GAME_OVER_MENU[1], self.screen_width, self.screen_height)
    
    # Background image will be stored in this variable
    self.background = None

    # Set the working directory (where we expect to find files) to the same
    # directory this .py file is in.
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)
  
  def setup(self):
    # Player setup
    self.player = player("img/player.png",self.screen_width/2,self.screen_height/2)

    # Sprite lists SETUP
    self.beer_list=arcade.SpriteList()
    self.vomit_list=arcade.SpriteList()

    beer_sprite=beer(self.screen_width, self.screen_height, self.screen_width//2, self.screen_height//2)
    self.current_beer_number = 1
    self.beer_list.append(beer_sprite)

    securitas_1 = Securitas("img/securitas.png",self.screen_width // 2 + 250,self.screen_height // 2 - 100,False)
    securitas_2 = Securitas("img/securitas.png",self.screen_width // 2 - 250,self.screen_height // 2 + 250,False)
    self.securitas_list=arcade.SpriteList()
    self.securitas_list.append(securitas_1)
    self.securitas_list.append(securitas_2)

    # Background loaded
    self.background = arcade.load_texture("img/map1_1280.png")

    # Window SETUP
    self.score=0
    self.total_time=0

    self.map = Map("maps/map1_wall.csv", self.screen_width, self.screen_height)

    self.physic_engines_list = list()

    self.physic_engines_list.append(arcade.PhysicsEngineSimple(self.player,self.map.wall_list))

    # Sounds effect setup
    securitas_upgrade_sound=arcade.load_sound("sounds/effects/securitasupgrade.wav")
    self.sounds_effects_list=dict()
    self.sounds_effects_list["securitasupgrade"]=securitas_upgrade_sound

    # Physic engines setup
    self.physic_engines_list.append(arcade.PhysicsEngineSimple(securitas_1,self.map.wall_list))
    self.physic_engines_list.append(arcade.PhysicsEngineSimple(securitas_2,self.map.wall_list))

  def on_draw(self): 
   
    arcade.start_render()

    # GameOver display
    if self.game_over :

      score=self.score*self.total_time

      # Game over with highscore display
      if self.game_over_isHighscore:
        output_position = "0" # TODO Implement position
        self.high_score_menu.addItem(POSITION_ITEM[0], POSITION_ITEM[1],POSITION_ITEM[2], output_position, POSITION_ITEM[4], POSITION_ITEM[5])
        output_score = f"{int(self.score)}"
        self.high_score_menu.addItem(SCORE_ITEM[0], SCORE_ITEM[1],SCORE_ITEM[2], output_score, SCORE_ITEM[4], SCORE_ITEM[5])
        self.high_score_menu.draw()

      # Game over witout highscore display
      else :
        output_score = f"{int(self.score)}"
        self.game_over_menu.addItem(SCORE_GAME_OVER_ITEM[0], SCORE_GAME_OVER_ITEM[1],SCORE_GAME_OVER_ITEM[2],
          output_score, SCORE_GAME_OVER_ITEM[4], SCORE_GAME_OVER_ITEM[5])
        self.game_over_menu.draw()
      

    # Menu display
    elif (self.menu):
      # Draw menu with specific values
      self.main_menu.draw()

    # Highscore display
    elif (self.highscores):
      # TODO: need to be improve because we parse highscore file in every draw() call ... Git blame JP :)
      list_highscore=take_scores()
      rank=1
      sorted_highscore=sorted(list_highscore.items(),key=operator.itemgetter(1),reverse=True)
      for pair in sorted_highscore :
        keys=re.sub('@','',pair[0])
        output=str(rank)+ " : " + keys + "  "+ str(pair[1])# + keys 
        self.high_scores_menu.addItem(INITIAL_HIGHSCORES[0], INITIAL_HIGHSCORES[1] - rank * (INITIAL_HIGHSCORES[2] + 10) / self.screen_height, 
          INITIAL_HIGHSCORES[2], output, INITIAL_HIGHSCORES[4], INITIAL_HIGHSCORES[5])
        rank+=1

      self.high_scores_menu.draw()

    # Game display
    else:
      # Background
      arcade.draw_texture_rectangle(self.screen_width // 2, self.screen_height // 2,
                                      self.screen_width, self.screen_height, self.background)
      
      # Sprites display
      self.beer_list.draw()
      self.vomit_list.draw()
      self.securitas_list.draw()
      self.player.draw()
      self.map.wall_list.draw()
      

      # Current time calculation
      minutes=int(self.total_time)//60
      seconds=int(self.total_time)%60
  
      # Score and current time display
      output_score=f"Score: {int(self.score*self.total_time)}"
      output_time=f"Time: {minutes:02d}:{seconds:02d}"
      arcade.draw_text(output_score,620,100,arcade.color.WHITE,18)
      arcade.draw_text(output_time,620,50,arcade.color.WHITE,18)

  def update(self, delta_time):
    # During the game
    if (self.game_over == False and self.menu==False and self.highscores==False):
      
      # Current time update
      self.total_time+=delta_time

      # Beers update
      self.beer_list.update()

      # vomits update
      for vomit_sprites in self.vomit_list : 
        vomit_sprites.life-=delta_time
        if vomit_sprites.life<0:
          vomit_sprites.kill()

      # Player update
      self.player.update(delta_time)

      # Change picture if drunk
      if self.player.BAC >= DRUNK_LEVEL_PLAYER and self.player.isDrunk == False:
        newPlayer = player("img/player_drunk.png",self.player.center_x,self.player.center_y,True)
        newPlayer.change_x = self.player.change_x
        newPlayer.change_y = self.player.change_y
        # self.player.kill()
        self.kill_properly(self.player, newPlayer)
        self.player = newPlayer

        
      # Securitas update img
      for secu in self.securitas_list:
        if secu.BAC >= ANGRY_SECURITAS_BAC and secu.isAngry == False:
          newSecuritas = Securitas("img/securitas_angry.png", secu.center_x, secu.center_y, True)
          self.kill_properly(secu, newSecuritas)
          self.securitas_list.append(newSecuritas)
          arcade.play_sound(self.sounds_effects_list["securitasupgrade"])
        elif secu.BAC < ANGRY_SECURITAS_BAC and secu.isAngry:
          newSecuritas = Securitas("img/securitas.png", secu.center_x, secu.center_y)
          self.kill_properly(secu, newSecuritas)
          self.securitas_list.append(newSecuritas) 

      # Securitas update   
      for secu in self.securitas_list:
        secu.update(delta_time)
        secu.check_if_player_around(self.player)
        secu.check_if_charge_player(self.player)

      # PHYSIC ENGINE UPDATE
      for physics_engine in self.physic_engines_list:
        physics_engine.update()

      # CHECK SECURITAS BLOCK IN WALLS AND CHANGE THEIR DIRECTION (MUST BE AFTER PHYSIC UPDATE AND SECURITAS UPDATE)
      for securitas in self.securitas_list:
        securitas.check_for_physic_engine_block()
        

      # Handler of collision securitas sprites with statics sprite
      for securitas_sprite in self.securitas_list:
        secu_vomit_hit_list = arcade.check_for_collision_with_list(securitas_sprite,self.vomit_list)
        secu_beer_hit_list = arcade.check_for_collision_with_list(securitas_sprite,self.beer_list)
        if len(secu_vomit_hit_list)>0:
          securitas_sprite.static_time=TIME_STATIC
          securitas_sprite.can_move=False
          securitas_sprite.change_x=0
          securitas_sprite.change_y=0
          securitas_sprite.BAC = 0
        for vomit_sprites in secu_vomit_hit_list:
          vomit_sprites.kill()
        for beer_sprites in secu_beer_hit_list:
          beer_sprites.kill()
          securitas_sprite.BAC+=1


      
      # generate current_beer_number 
      if self.total_time//BEER_GENERATION_COEFF<1:
        if self.total_time > 30 and self.total_time < 60:
          self.current_beer_number = 2
        else:
          self.current_beer_number = 1 
      else :
         self.current_beer_number = self.total_time//BEER_GENERATION_COEFF

      # Beer boost 
      self.current_beer_number += (self.player.BAC//BEER_BOOST_COEFF if self.player.BAC//BEER_BOOST_COEFF <= MAX_BAC_BOOST else SECOND_STEP_MAX_BAC_BOOST if self.total_time > TOTAL_TIME_SECOND_STEP else MAX_BAC_BOOST)

      # Beer generation
      if len(self.beer_list) < self.current_beer_number and random.randint(0, BEER_DELAY) == 2:
        newBeer = beer(self.screen_width, self.screen_height)
        self.beer_list.append(newBeer) 

      # Handle beers collapsed by player
      beer_hit_list = arcade.check_for_collision_with_list(self.player,self.beer_list)
      for beer_sprite_hit in beer_hit_list:
        beer_sprite_hit.kill()
        self.player.BAC+=1
 
      # generate current_beer_number 
      if self.total_time//BEER_GENERATION_COEFF<1:
        if self.total_time > 30 and self.total_time < 60:
          self.current_beer_number = 2
        else:
          self.current_beer_number = 1 
      else :
         self.current_beer_number = self.total_time//BEER_GENERATION_COEFF

      # Beer boost 
      self.current_beer_number += (self.player.BAC//BEER_BOOST_COEFF if self.player.BAC//BEER_BOOST_COEFF <= MAX_BAC_BOOST else SECOND_STEP_MAX_BAC_BOOST if self.total_time > TOTAL_TIME_SECOND_STEP else MAX_BAC_BOOST)

      # Beer generation
      if len(self.beer_list) < self.current_beer_number and random.randint(0, BEER_DELAY) == 2:
        newBeer = beer(self.screen_width, self.screen_height)
        self.beer_list.append(newBeer) 

      # Handle player if he walks on a vomit
      vomit_hit_list = arcade.check_for_collision_with_list(self.player,self.vomit_list) 
      for vommit in vomit_hit_list:
        if self.player.invincible == False:
          vommit.kill()
          self.player.can_move=False
          self.player.static_time=TIME_STATIC

      # Result of a collision between a player and a securitas
      # # GameOver menu opened
      # # highscore handler       
      securitas_hit_list = arcade.check_for_collision_with_list(self.player,self.securitas_list)
      if len(securitas_hit_list)>0 :
        self.game_over=True   
        self.score=self.score*self.total_time
        highscore=take_scores()
        if len(highscore)<10:
          self.game_over_isHighscore=True
          while self.username in highscore:
            self.username+="@"
          highscore[self.username]=int(self.score)
          save_score(highscore)
        else:
          if self.score>highscore[min(highscore,key=highscore.get)]:
            self.game_over_isHighscore=True
            del highscore[min(highscore,key=highscore.get)]
            while self.player.username in highscore:
              self.player.username+="@"
            highscore[self.username]=int(self.score)
            save_score(highscore)

  # Result of all key pressed possibility
  def on_key_press(self, key, modifiers):
    if(self.game_over==False, self.menu==False, self.highscores==False):
      if(self.player.can_move):
        if key == arcade.key.UP:
          self.player.change_y = MOVEMENT_SPEED
        if key == arcade.key.DOWN:
          self.player.change_y = -MOVEMENT_SPEED
        if key == arcade.key.LEFT:
          self.player.change_x = -MOVEMENT_SPEED
        if key == arcade.key.RIGHT:
          self.player.change_x = MOVEMENT_SPEED


  # Result of all key released possibility
  def on_key_release(self, key, modifiers):
    if(self.game_over==False, self.menu==False, self.highscores==False):
      if key == arcade.key.UP or key == arcade.key.DOWN:
        self.player.change_y = 0
      if key == arcade.key.LEFT or key == arcade.key.RIGHT:
        self.player.change_x = 0
      if key == arcade.key.TAB and self.player.BAC>0:
          vomit_sprite=vomit(self.player.center_x,self.player.center_y)
          self.score+=self.player.BAC
          self.vomit_list.append(vomit_sprite)
          if self.player.isDrunk:
            newPlayer = player("img/player.png",self.player.center_x,self.player.center_y)
            newPlayer.change_x = self.player.change_x
            newPlayer.change_y = self.player.change_y
            # self.player.kill()
            self.kill_properly(self.player, newPlayer)
            self.player = newPlayer
          else:
            self.player.BAC=0

            
          self.player.invincible = True
          self.player.invincible_time=TIME_INVINCIBLE
          
  # Mouse handler        
  def on_mouse_press(self,x,y,button,modifiers):
    
    # During GameOver display 
    if self.game_over :
      if self.game_over_isHighscore:
        for item in self.high_score_menu.items:
          if item.clickable and item.handleClick(x,y):
            if item.text == "Rejouer":
              self.setup()
              self.game_over = False
            elif item.text == "Highscores":
              self.game_over = False
              self.highscores = True
            elif item.text == "Menu":
              self.game_over=False
              self.menu=True
      else:
        for item in self.game_over_menu.items:
          if item.clickable and item.handleClick(x,y):
            if item.text == "Rejouer":
              self.setup()
              self.game_over = False
            elif item.text == "Highscores":
              self.game_over = False
              self.highscores = True
            elif item.text == "Menu":
              self.game_over=False
              self.menu=True
    
    # During menu display 
    elif self.menu:
      for item in self.main_menu.items:
        if item.clickable and item.handleClick(x,y):
          if item.text == "Jouer":
            self.setup()
            self.menu=False
          elif item.text == "Highscores":
            self.menu=False
            self.highscores=True
          elif item.text == "Quitter":
            arcade.quick_run(0.5)
    
    # During highscore display
    elif self.highscores:
      for item in self.high_scores_menu.items:
        if item.clickable and item.handleClick(x,y):
          if item.text == "Menu":
            self.highscores=False
            self.menu=True
    
  def kill_properly(self, sprite, newSprite):
    for physics_engine in self.physic_engines_list:
      if (physics_engine.player_sprite == sprite):
        self.physic_engines_list.remove(physics_engine)
    sprite.kill()
    self.physic_engines_list.append(arcade.PhysicsEngineSimple(newSprite, self.map.wall_list))
    

def main():
    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
  main()
