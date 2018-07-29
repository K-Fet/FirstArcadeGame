# -------------- MENU DATA --------------

# An item is an array representing the values of the static_item class constructor
# As a result this array follows this syntax: [x_proportion: float, y_proportion: float, text: string, color: string]
# 
# To implement a new color, please refere to the static_item.getArcadeColor()

# MAIN MENU
MAIN_MENU_ITEM_FONT_SIZE = 36

PLAY_ITEM = [1/2,49/72,MAIN_MENU_ITEM_FONT_SIZE,"Jouer","white"]
HIGHSCORE_ITEM = [1/2,31/72,MAIN_MENU_ITEM_FONT_SIZE,"Highscores","white"]
QUIT_ITEM = [1/2,13/72,MAIN_MENU_ITEM_FONT_SIZE,"Quitter","white"]

MAIN_MENU = [
  [PLAY_ITEM, HIGHSCORE_ITEM, QUIT_ITEM]
]

def generateValuesMainMenu():
  return ['','','']
