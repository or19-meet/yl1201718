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
	color = (random.random(), random.random(), random.random())
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)

new_Ball=Ball(x,y,dx,dy,radius,color)
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
				random_x = random.randint(screen_random1_x,screen_random2_x)
				random_y = random.randint(screen_random1_y,screen_random2_y)
				random_dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while random_dx == 0:
					random_dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				random_dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while random_dy == 0:
					random_dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

				if radiusA > radiusB:
					ball_b.goto(random_x,random_y)
					ball_b.dx = random_dx
					ball_b.dy = random_dy
					ball_b.r = radius
					ball_b.shapesize(ball_b.r/10)
					ball_b.color = color
					ball_a.r += 0.5
					ball_a.shapesize(ball_a.r/10)
					
				elif radiusA < radiusB:
					ball_a.goto(random_x,random_y)
					ball_a.dx = random_dx
					ball_a.dy = random_dy
					ball_a.r = radius
					ball_a.shapesize(ball_a.r/10)
					ball_a.color = color
					ball_b.r += 0.5
					ball_b.shapesize(ball_b.r/10)


def check_myball_collision():
	for ball in balls:
		random_x = random.randint(screen_random1_x,screen_random2_x)
		random_y = random.randint(screen_random1_y,screen_random2_y)
		random_dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
		while random_dx == 0:
			random_dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
		random_dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
		while random_dy == 0:
			random_dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
		radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
		color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		if check_collide(MY_BALL,ball) == True:
			radiusC = MY_BALL.r
			radiusD = ball.r

			if MY_BALL.r < ball.r:
				print("you suck, GAME OVER")
				return 	False
			else:
				MY_BALL.r += 2
				MY_BALL.shapesize(MY_BALL.r/10)
				score += 1
				scoret.pu()
				scoret.goto(0,250)
				scoret.clear()
				scoret.write("SCORE: " + str(score),align="center",font=("Arial", 20, "normal"))
				ball.goto(random_x,random_y)
				ball.dx = random_dx
				while ball.dx == 0:
					ball.dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				ball.dy = random_dy
				while ball.dy == 0:
					ball.dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				ball.r = radius
				ball.shapesize(ball.r/10)
				ball.color = color
	return True

def movearound(event):
	x1 = event.x - screen_width
	y1 = screen_height - event.y
	MY_BALL.goto(x1,y1)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING == True:
	if SCREEN_WIDTH != (turtle.getcanvas().winfo_width()/2) or SCREEN_HEIGHT != (turtle.getcanvas().winfo_height()/2): 
		SCREEN_WIDTH =(turtle.getcanvas().winfo_width()/2)
		SCREEN_HEIGHT = (turtle.getcanvas().winfo_height()/2)
	move_all_balls()
	# check_all_balls_collision()
	if check_myball_collision() == False:
		turtle.goto(0,0)
		turtle.write("you suck, GAME OVER!",align="center",font=("Arial", 50, "normal"))
		time.sleep(5)
		turtle.bye()
	getscreen().update()
	time.sleep(sleep)
mainloop()
