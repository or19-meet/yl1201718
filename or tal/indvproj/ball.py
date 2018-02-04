from turtle import *
import turtle
import random

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,colour):
		Turtle.__init__(self)
		self.x=x
		self.y=y
		self.penup()
		self.setposition(x,y)  #each time we use this we relocate
		self.dx = dx
		self.dy = dy
		self.radius = radius
		self.shape("circle")
		self.shapesize(radius/10)
		
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)

	def move(self,screen_width,screen_height):
		current_x=self.x
		current_y=self.y
		new_x=current_x+self.dx
		new_y=current_y+self.dy
		right_side_ball=new_x+self.radius
		left_side_ball=new_x-self.radius
		up_side_ball=new_y+self.radius
		down_side_ball=new_y+self.radius
		self.x, self.y = new_x,new_y
		if right_side_ball >= screen_width:
			self.dx-=self.dx
		if left_side_ball <= screen_width:
			self.dx-=self.dx
		if up_side_ball >= screen_height:
			self.dy-=self.dy
		if down_side_ball <= screen_height:
			self.dy-=self.dy


