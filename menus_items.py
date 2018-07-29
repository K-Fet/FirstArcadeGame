# -------------- MENU DATA --------------

# An item is an array representing the values of the static_item class constructor
# As a result this array follows this syntax: [x_proportion: float, y_proportion: float, text: string, color: string]
# 
# To implement a new color, please refere to the static_item.getArcadeColor()

# MAIN MENU

PLAY_ITEM = [1/2,11/16,"JOUER","white"]
HIGHSCORE_ITEM = [1/2,11/16,"HIGH SCORES","white"]
QUIT_ITEM = [1/2,11/16,"QUITTER","white"]

MAIN_MENU = [
  [PLAY_ITEM, HIGHSCORE_ITEM, QUIT_ITEM]
]

def generateValuesMainMenu():
  return ['']
