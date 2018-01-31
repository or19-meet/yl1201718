from turtle import *
import turtle
import time
import random
from ball import Ball
colormode(255)
hideturtle()
tracer(0)


RUNNING=True 
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(0,0,0,0,12,"blue")

NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DX=-5

MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

balls=[]
for i in range (NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dx==0:
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)

		dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dy==0:
		dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	colour = (random.random(), random.random(), random.random())
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)

new_Ball=Ball(x,y,dx,dy,radius,colour)
balls.append(new_Ball)

def move_all_balls():
	for variable in range(NUMBER_OF_BALLS):
		balls[variable].move(SCREEN_WIDTH,SCREEN_HEIGHT)

def check_collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False

	distance = math.sqrt(math.pow(ball_a.x - ball_b.x, 2) + math.pow(ball_a.y - ball_b.y, 2))

	if distance +10 < ball_a.r+ball_b.r:
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in balls:
		for ball_b in balls:
			if collide(ball_a,ball_b)==True:
				radiusA = ball_a.r 
				radiusB = ball_b.r
				



