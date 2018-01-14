from turtle import *

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,colour):
		Turtle.__init__(self)
		self.penup()
		self.setposition(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		turtle.shape("circle")
		self.shapesize(r/10)
		
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.colour(r,g,b)

		def move(self):
			current_x=self.xcor()
			current_y=self.ycor()

