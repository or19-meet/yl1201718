from turtle import *
import random

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)


ball1=Ball(3,"blue",12)
ball2=Ball(2, "red", 8)

def check_collision(ball1, ball2):
	





mainloop()