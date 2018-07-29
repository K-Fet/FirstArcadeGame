import arcade

class StaticItem:
  # This class represent responsive menu item. It works with proportion instead of real position.
  # 0 < width_proportion < 1
  # 0 < height_proportion < 1
  # color could be 'white'
  def __init__(self, width_proportion, height_proportion, text, color, screen_width, screen_heigth):
    self.x = width_proportion * screen_width
    self.y = height_proportion * screen_heigth
    self.height = int(screen_heigth / 14)
    self.width = int(len(text) * 0.4 * self.height) # I don't understand why ?
    self.text = text
    self.color = self.getArcadeColor(color)

  def draw(self, value):
    output = f"{self.text + value}"
    arcade.draw_text(output, self.x, self.y, self.color, self.width, self.height, align="center",anchor_x="center",anchor_y="center")

  def getArcadeColor(self, color):
    if color == "white":
      return arcade.color.WHITE
