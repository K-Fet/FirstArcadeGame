# -------------- MENU DATA --------------

## Item
# An item is an array representing the values of the static_item class constructor
# An item must match: [x_proportion, y_proportion, fontSize, text, color, clickable]
# Please see the static_item constructor if you want more information.
# To implement a new color, please refere to the static_item.getArcadeColor() method
#
## Menu
# A menu is composed by an array of item and a backgrounUrl

#########   MAIN MENU   #########
MAIN_MENU_ITEM_FONT_SIZE = 36

PLAY_ITEM = [1/2,49/72,MAIN_MENU_ITEM_FONT_SIZE,"Jouer","black",True]
HIGHSCORE_ITEM = [1/2,31/72,MAIN_MENU_ITEM_FONT_SIZE,"Highscores","black",True]
QUIT_ITEM = [1/2,13/72,MAIN_MENU_ITEM_FONT_SIZE,"Quitter","black",True]

MAIN_MENU = [
  [PLAY_ITEM, HIGHSCORE_ITEM, QUIT_ITEM],
  "img/menu/main_menu.png"
]

#########   HIGHSCORES  #########
MENU_ITEM = [10/128,40/720,24,"Menu","black",True]
INITIAL_HIGHSCORES = [1/2,47/72,24,"USELESS_HERE","black",False]

HIGHSCORES_MENU = [
  [MENU_ITEM],
  "img/menu/highscores.png"
]

#########   HIGHSCORE  #########
RESTART_ITEM = [116/128,70/720,24,"Rejouer","black",True]
HIGHSCORES_ITEM = [68/128,40/720,24,"Highscores","black",True]
SCORE_ITEM = [81/128,255/720,24,"USELESS_HERE","black",True]
POSITION_ITEM = [81/128,320/720,24,"USELESS_HERE","black",True]

HIGHSCORE_MENU = [
  [MENU_ITEM, RESTART_ITEM, HIGHSCORES_ITEM],
  "img/menu/highscore.png"
]

#########   GAME OVER  #########
SCORE_GAME_OVER_ITEM = [81/128,300/720,24,"USELESS_HERE","black",True]

GAME_OVER_MENU = [
  [MENU_ITEM, RESTART_ITEM, HIGHSCORES_ITEM],
  "img/menu/game_over.png"
]
