import arcade
from data import *
import random

class beer(arcade.Sprite):
	def __init__(self, screen_width, screen_height, x=None, y=None):
		super().__init__("img/beer.png",SPRITE_SCALING_BEER)
		# Generate map_beer from the csv 
		self.map_beer = self.get_map("maps/map1_beer.csv")
		# Check if the coordinates passed to the constructor are valid
		if (x != None and y != None):
			isOk = self.check_beer_position(screen_width, screen_height, x, y)
		# Init isOk to enter in while loop
		else:
			isOk = False
		while (isOk == False):
			# Generate random x and y while they're not valid coordinates
			x = random.randrange(0, screen_width)
			y = random.randrange(0, screen_height)
			isOk = self.check_beer_position(screen_width, screen_height, x, y)
		# x and y are valid, create a little offset to avoid beer on walls
		x = x + 10 if x < screen_width//2 else x - 10
		y = y + 10 if y < screen_height//2 else y - 10
		self.center_x=x
		self.center_y=y
		
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

	def check_beer_position(self, screen_width, screen_height, x, y):
		# transformed_x is between 0 - 64 
		transformed_x = (x*64)//screen_width 
		# transformed_y : same as transformed_x but y in the map_beer is ascendant whereas y in center_x is descendant 
		transformed_y = len(self.map_beer) - ((y*36)//screen_height + 1)
		# Check if the beer can appear here
		if (self.map_beer[transformed_y][transformed_x] == 0):
			return True
		else:
			return False
