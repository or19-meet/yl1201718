from turtle import *

class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shape("Square")
		self.shapesize(size)

	def random_colour(self):
		r=random.randit(0,225)
		g=random.randit(0,225)
		b=random.randit(0,225)
		self.colour(r,g,b)
		