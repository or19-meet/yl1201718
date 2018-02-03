from turtle import *
import turtle
import random


class Ball(Turtle):
    def init(self, x, y, dx, dy, r, color):
        turt = Turtle()  # creating a new Turtle object
        self.penup()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color = color
        self.setposition(self.x, self.y)  # each time we use this we relocate
        turt.shape("circle")
        self.shapesize(r / 10)

        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def move(self, screen_width, screen_height):
        current_x = self.x
        current_y = self.y
        new_x = current_x + self.dx
        new_y = current_y + self.dy
        right_side_ball = new_x + self.r
        left_side_ball = new_x - self.r
        up_side_ball = new_y + self.r
        down_side_ball = new_y + self.r
        self.x, self.y = new_x, new_y
        if right_side_ball >= screen_width:
            self.dx -= self.dx
        if left_side_ball <= screen_width:
            self.dx -= self.dx
        if up_side_ball >= screen_height:
            self.dy -= self.dy
        if down_side_ball <= screen_height:
            self.dy -= self.dy