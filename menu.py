import arcade
from static_item import * 

class Menu:
  def __init__(self, items, generateValue, screen_width, screen_heigth):
    self.generateValue = generateValue
    self.items = []

    for item in items:
      self.items.append(StaticItem(item[0],item[1],item[2],item[3],item[4],item[5],screen_width,screen_heigth))

  def draw(self, menuValue):
    for index, item in  enumerate(self.items):
      item.draw(menuValue[index])
