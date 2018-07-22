import arcade
from data import *
import math

class stripline():
	def __init__(self, points):
		self.points = points
		self.points_list=list()
		
		x1=int(points[0][0])
		x2=int(points[1][0])
		y1=points[0][1]
		y2=points[1][1]

		distance=math.sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))
		number_of_points=int(0.7*distance)
		y=0
		x=0

		for i in range(number_of_points):
			if x1 <= x2 and y1 <= y2:
				x = x1 + i * ( ( x2 - x1 ) / number_of_points )
				y = y1 + i * ( ( y2 - y1 ) / number_of_points )
			if x1 >= x2 and y1 <= y2:
				x = x1 - i * ( ( x1 - x2 ) / number_of_points )
				y = y1 + i * ( ( y2 - y1 ) / number_of_points )
			if x1 >= x2 and y1 >= y2:
				x = x1 - i * ( ( x1 - x2 ) / number_of_points )
				y = y1 - i * ( ( y1 - y2 ) / number_of_points )
			if x1 <= x2 and y1 >= y2:
				x = x1 + i * ( ( x2 - x1 ) / number_of_points )
				y = y1 - i * ( ( y1 - y2 ) / number_of_points )
			coord=(x,y)
			self.points_list.append(coord)

			# if y1 == y2 and y1 == 186:
			# 	print(number_of_points)
			# 	print("Point 1 ",x1,y1)
			# 	print("Point 2 ",x2,y2)
			# 	print("Points list ",self.points_list)
	
	# CHECK COLLISSION WITH OBJECT (x,y)
	#
	# player_x: x of the player
	# player_y: y of the player
	# return disable: [Bool,Bool,Bool,Bool] 
	# representing [DISABLE_LEFT,DISABLE_RIGHT,DISABLE_UP,DISABLE_BOTTOM]
	#
	def check_for_collisions_with_object(self, object_x, object_y):
		disabledKeys = [False, False, False, False]
		for point in self.points_list:
			x = point[0]
			y = point[1]

			dist_x = x - object_x
			dist_y = y - object_y

			distance=math.sqrt((y-object_y)*(y-object_y)+(x-object_x)*(x-object_x))	

			# Fix
			# if y == 186:
			# 	print("x y: ",x,y)
			# 	print("Distance : ",distance)
			# 	print("dist_x : ",dist_x)
			# 	print("dist_y : ",dist_y)

			if distance < 30:
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
				if disabledKeys != [False,False,False,False]:
					return disabledKeys
		return [False,False,False,False]

		

	def draw(self):
		arcade.draw_line_strip(self.points, arcade.color.BLACK)


