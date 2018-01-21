import turtle 
import time
import random
import Ball

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