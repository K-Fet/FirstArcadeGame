import arcade

class StaticItem:
  # This class represent responsive menu item. It works with proportion instead of real position.
  # 0 < x_proportion < 1
  # 0 < y_proportion < 1
  # color could be 'white'
  def __init__(self, x_proportion, y_proportion, height_proportion, text, color, screen_width, screen_heigth):
    self.x = x_proportion * screen_width
    self.y = y_proportion * screen_heigth
    self.height = height_proportion * screen_heigth
    self.text = text
    self.color = self.getArcadeColor(color)

  def draw(self, value):
    output = f"{self.text + value}"
    arcade.draw_text(output,self.x,self.y,self.color,self.height,align="center",anchor_x="center",anchor_y="center")

  def getArcadeColor(self, color):
    if color == "white":
      return arcade.color.WHITE
