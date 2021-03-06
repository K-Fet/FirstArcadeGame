import arcade

class StaticItem:
  # This class represent responsive menu item. It works with proportion instead of real position.
  # x_proportion: 0 < x_proportion < 1
  # y_proportion: 0 < y_proportion < 1
  # text: the text of this item
  # color: a string representing a color. It must be implemented in the getArcadeColor() method !
  # clickable: define if this item is clickable
  def __init__(self, x_proportion, y_proportion, fontSize, text, color, clickable, screen_width, screen_heigth):
    self.x = x_proportion * screen_width
    self.y = y_proportion * screen_heigth
    self.fontSize = fontSize
    self.text = text
    self.color = self.getArcadeColor(color)
    self.clickable = clickable

    # Compute width / height based on fontSize
    self.height = self.fontSize
    self.width = 0.4 * self.fontSize * len(text)

  def draw(self):
    output = f"{self.text}"
    arcade.draw_text(output,self.x,self.y,self.color,self.fontSize,align="center",anchor_x="center",anchor_y="center")

  def getArcadeColor(self, color):
    if color == "white":
      return arcade.color.WHITE
    if color == "black":
      return arcade.color.BLACK
  
  def handleClick(self, x: int, y: int) -> bool:
    if x < self.x + self.width and x > self.x - self.width and y < self.y + self.height and y > self.y - self.height:
      return True
    return False
