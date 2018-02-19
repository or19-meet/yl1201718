import turtle
from turtle import *
import random
import math


# colormode(255)
class Ball(Turtle):
    def __init__(self, x, y, dx, dy, radius, color):
        Turtle.__init__(self)
        self.pu()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.ashugauoash = color
        self.goto(x, y)
        self.color(color)
        self.shape("circle")
        self.shapesize(radius / 10)

    def setdx(self, dx):
        self.dx = dx

    def setdy(self, dy):
        self.dy = dy

    def setRadius(self, radius):
        self.radius = radius
        self.shapesize(radius / 10)
    def setColor(self, color):
        self.color(color)

    def move(self, screen_width, screen_hight):
        current_x = self.xcor()
        current_y = self.ycor()

        new_x = current_x + self.dx
        new_y = current_y + self.dy

        right_side_ball = current_x + self.radius
        left_side_ball = current_x - self.radius
        upper_side_ball = current_y + self.radius
        lower_side_ball = current_y - self.radius

        if (left_side_ball <= (-screen_width)):
            new_x = current_x - self.dx
            self.setdx(-self.dx)
        else:
            new_x = current_x + self.dx

        if (right_side_ball >= (screen_width)):
            new_x = current_x - self.dx
            self.setdx(-self.dx)
        else:
            new_x = current_x + self.dx

        if (upper_side_ball >= (screen_hight)):
            new_y = current_y - self.dy
            self.setdy(-self.dy)
        else:
            new_y = current_y + self.dy

       

        self.setx(new_x)
        self.sety(new_y)


