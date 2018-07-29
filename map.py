import arcade

class Map:
  def __init__(self, filename_wall,screen_width,screen_height):
    self.map_array_wall = self.get_map(filename_wall)
    self.wall_list = self.generateWallList(screen_width,screen_height)

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

  def generateWallList(self, screen_width, screen_height, scalling=1):
    wall_list = arcade.SpriteList()
    for row_index, row in enumerate(self.map_array_wall):
      for column_index, item in enumerate(row):

        # For this map, the numbers represent:
        # -1 = empty
        # 0  = wall
        if item == -1:
          continue
        elif item == 0:
          wall = arcade.Sprite("img/wall.png", screen_width / 1280)
        wall.right = (column_index + 1) * (screen_width // 64)
        wall.top = screen_height - (row_index) * (screen_height// 36)
        wall_list.append(wall)

    return wall_list
