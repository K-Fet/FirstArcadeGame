import arcade
from data import *

class stripline():
	def __init__(self, points):
		print("stripline init")
		self.points = points
		# self.center_x = (points[0][0] + points[1][0]) / 2
		# self.center_y = (points[0][1] + points[1][1]) / 2  

	def draw(self):
		arcade.draw_line_strip(self.points, arcade.color.BLACK)

