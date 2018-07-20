import arcade
from data import *

class stripline():
	def __init__(self, points):
		print("stripline init")
		self.points = points
		# self.center_x = (points[0][0] + points[1][0]) / 2
		# self.center_y = (points[0][1] + points[1][1]) / 2
		self.points_list=list()
		
		x1=int(points[0][0])
		x2=int(points[1][0])
		y1=points[0][1]
		y2=points[1][1]
		y=0
		x=0
		dir_coeff=(y2-y1)/(x2-x1)
		for x in range (x1,x2,1):
			y=int(y1+dir_coeff*(x-x1))
			coord=(x,y)
			self.points_list.append(coord)
		
		print(self.points_list)

	def draw(self):
		arcade.draw_line_strip(self.points, arcade.color.BLACK)



