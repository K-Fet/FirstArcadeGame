import arcade

class StaticItem:
  # This class represent responsive menu item. It works with proportion instead of real position.
  # 0 < x_proportion < 1
  # 0 < y_proportion < 1
  # color could be 'white'
  def __init__(self, x_proportion, y_proportion, fontSize, text, color, screen_width, screen_heigth):
    self.x = x_proportion * screen_width
    self.y = y_proportion * screen_heigth
    self.fontSize = fontSize
    self.text = text
    self.color = self.getArcadeColor(color)

    # Compute width / height
    self.height = self.fontSize
    self.width = 0.4 * self.fontSize * len(text)
    print(self.width, self.height)
    print("-----------------------")

  def draw(self, value):
    output = f"{self.text + value}"
    arcade.draw_text(output,self.x,self.y,self.color,self.fontSize,align="center",anchor_x="center",anchor_y="center")

  def getArcadeColor(self, color):
    if color == "white":
      return arcade.color.WHITE
  
  def handleClick(self, x: int, y: int):
    if x < self.x + self.width and x > self.x - self.width and y < self.y + self.height and y > self.y - self.height:
      return True
    return False
