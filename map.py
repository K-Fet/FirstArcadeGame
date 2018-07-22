import arcade

class Map:
  def __init__(self, filename):
    self.map_array = self.get_map(filename)
    self.wall_list = self.generateWallList()

  def get_map(self, filename):
    """
    This function loads an array based on a map stored as a list of
    numbers separated by commas.
    """
    map_file = open(filename)
    map_array = []
    for line in map_file:
      line = line.strip()
      map_row = line.split(",")
      for index, item in enumerate(map_row):
        map_row[index] = int(item)
      map_array.append(map_row)
    return map_array

  def generateWallList(self, scalling=1):
    wall_list = arcade.SpriteList()
    for row_index, row in enumerate(self.map_array):
      for column_index, item in enumerate(row):

        # For this map, the numbers represent:
        # -1 = empty
        # 0  = wall
        if item == -1:
          continue
        elif item == 0:
          wall = arcade.Sprite("img/wall.png", scalling)

        wall.right = (column_index + 1) * 20
        wall.top = (len(row) - row_index) * 20 - 560
        wall_list.append(wall)

    return wall_list
