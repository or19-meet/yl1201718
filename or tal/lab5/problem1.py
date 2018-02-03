from turtle import *
import random
colormode(255)

class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)

		self.shape("square")
		self.shapesize(size)

	def random_color(self):
		r=random.randint(0,225)
		g=random.randint(0,225)
		b=random.randint(0,225)
		self.color(r,g,b)

S=Square(20)
S.random_color()

# mainloop()

class Rectangle(Turtle):
	def __init__(self, width, height):
		Turtle.__init__(self)

		self.width=width
		self.height=height

		register_shape("rectangle",     

