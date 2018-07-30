import arcade
from static_item import * 

class Menu:
  def __init__(self, items, backgroundUrl, screen_width, screen_height):
    self.items = []
    self.background = arcade.load_texture(backgroundUrl)

    self.screen_width = screen_width
    self.screen_height = screen_height

    for item in items:
      self.items.append(StaticItem(item[0],item[1],item[2],item[3],item[4],item[5],screen_width,screen_height))

  def draw(self):
    # Background
    arcade.draw_texture_rectangle(self.screen_width // 2, self.screen_height // 2,
      self.screen_width, self.screen_height, self.background)

    # Menu items
    for item in self.items:
      item.draw()
  
  def addItem(self, x_proportion, y_proportion, fontSize, text, color, clickable):
    self.items.append(StaticItem(x_proportion, y_proportion, fontSize, text, color, clickable,self.screen_width,self.screen_height))
