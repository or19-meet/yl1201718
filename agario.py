import turtle 
import time
import random
import Ball
turtle.colormode(255)

turtle.tracer()
turtle.hideturtle()

RUNNING=True 
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(0,0,2,3,12,"blue")

NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_RADIUS=5
MINIMUM_BALL_DY=5
MAXIMUM_BALL_DY=-5

BALLS=[]
for i in range (NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	while dx==0:
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)

	dy = random.randint( MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dy==0:
		dy = random.randint( MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	colour = (random.random(), random.random(), random.random())
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)

new_Ball=Ball(x,y,dx,dy,radius,colour)
BALLS.append(new_Ball)

def move_all_balls 