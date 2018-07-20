import arcade
from data import *

class stripline():
	def __init__(self, points):
		print("stripline init")
		self.points = points
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
	
	def check_for_collisions_with_player(self, player_x, player_y):
		disabledKeys = [False, False, False, False]
		for point in self.points_list:
			x = point[0]
			y = point[1]
			dist_x = x - player_x
			dist_y = y - player_y
			if abs(dist_x) < 20 and abs(dist_y) < 20:
				if (dist_x > 0): 
					disabledKeys[1] = True 
					if disabledKeys[0] : disabledKeys[0] = False
				if (dist_x < 0): 
					disabledKeys [0] = True
					if disabledKeys[1] : disabledKeys[1] = False
				if (dist_y > 0): 
					disabledKeys[2] = True
					if disabledKeys[3] : disabledKeys[3] = False
				if (dist_y < 0): 
					disabledKeys[3] = True
					if disabledKeys[2] : disabledKeys[2] = False
		return disabledKeys


		

	def draw(self):
		arcade.draw_line_strip(self.points, arcade.color.BLACK)


