from turtle import *
import turtle
import random
import math
import time
from ball import Ball

turtle.colormode(255)
turtle.tracer(0)
turtle.hideturtle()
RUNNING=True
timer=5000
SLEEP=0.0065
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_WIDTH_MINUS=-turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
SCREEN_HEIGHT_MINUS = -turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(100,100,2,1,40,"blue")
evil_ball=Ball(150,50,3,4,10,"black")
original_radius=MY_BALL.radius
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS =10
MAXIMUM_BALL_RADIUS =50
MINIMUM_BALL_DX =-5
MAXIMUM_BALL_DX =5
MINIMUM_BALL_DY =-5
MAXIMUM_BALL_DY =5
turtle.register_shape("life.gif")
life_counter=3
heart_size=50
FIRST=int(SCREEN_WIDTH_MINUS + MAXIMUM_BALL_RADIUS)
SECOND=int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
BALLS=[]
heart_pos_list=[]
heart_stamp_list=[]

#life system:
turtle.showturtle()
life=turtle.clone()
life.shape("life.gif")
life.penup()
life.goto(-180,200)
life2=life.clone()
life2.goto(-220,200)
life3=life.clone()
life3.goto(-260,200)
turtle.hideturtle()
getscreen().update()

for i in range(NUMBER_OF_BALLS):
    x=random.randint(FIRST,SECOND)
    y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
    dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
    while dx==0:
        dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    while dy==0:
        dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY) 
    radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    r=random.randint(0,225)
    g=random.randint(0,225)
    b=random.randint(0,225)
    color=(r,g,b)
    balll=Ball(x,y,dx,dy,radius,color)
    BALLS.append(balll)

def move_all_balls():
    for i in BALLS:
        i.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    evil_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
    if ball_a==ball_b:
        return False
    DISTANCE_BETWEEN_CORES=math.sqrt((ball_a.xcor()-ball_b.xcor())**2+(ball_a.ycor()-ball_b.ycor())**2)
    if DISTANCE_BETWEEN_CORES+10<=ball_a.radius+ball_b.radius:
        return True
    else:
        return False
def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a,ball_b)==True:
                radius_a=ball_a.radius
                radius_b=ball_b.radius    
                x_coordinate=random.randint(FIRST,SECOND)
                y_coordinate=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
                x_axis_speed=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                while x_axis_speed==0:
                    x_axis_speed=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                y_axis_speed=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                while y_axis_speed==0:
                    y_axis_speed=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY) 
                radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                r=random.randint(0,225)
                g=random.randint(0,225)
                b=random.randint(0,225)
                color=(r,g,b)
                if radius_a<radius_b:
                    ball_a.goto(x_coordinate,y_coordinate)
                    ball_a.dx=x_axis_speed
                    ball_a.dy=y_axis_speed
                    ball_a.radius=radius
                    ball_a.shapesize(radius/10)
                    ball_a.color(color)
                    ball_b.radius=ball_b.radius+1
                    ball_b.shapesize(ball_b.radius/10)
                else:
                    ball_b.goto(x_coordinate,y_coordinate)
                    
                    ball_b.dx=x_axis_speed
                    ball_b.dy=y_axis_speed
                    ball_b.radius=radius
                    ball_b.shapesize(radius/10)
                    ball_b.color(color)
                    ball_a.radius=ball_a.radius+1
                    ball_a.shapesize(ball_a.radius/10)

def check_myball_collision():
    for i in BALLS:
        if collide(i,MY_BALL)==True:
            if MY_BALL.radius>i.radius:
                    x_coordinate=random.randint(FIRST,SECOND)
                    y_coordinate=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
                    x_axis_speed=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                    while x_axis_speed==0:
                        x_axis_speed=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                    y_axis_speed=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                    while y_axis_speed==0:
                        y_axis_speed=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY) 
                    radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                    r=random.randint(0,225)
                    g=random.randint(0,225)
                    b=random.randint(0,225)
                    color=(r,g,b)
                    i.goto(x_coordinate,y_coordinate)                    
                    i.dx=x_axis_speed
                    i.dy=y_axis_speed
                    i.radius=radius
                    i.shapesize(radius/10)
                    i.color(color)
                    MY_BALL.radius=MY_BALL.radius+1
                    MY_BALL.shapesize(MY_BALL.radius/10)
                    print("i ate")
                    return True
            if MY_BALL.radius<i.radius:
                x_coordinate=random.randint(FIRST,SECOND)
                y_coordinate=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
                x_axis_speed=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                while x_axis_speed==0:
                    x_axis_speed=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                y_axis_speed=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                while y_axis_speed==0:
                    y_axis_speed=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY) 
                radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                r=random.randint(0,225)
                g=random.randint(0,225)
                b=random.randint(0,225)
                color=(r,g,b)
                i.goto(x_coordinate,y_coordinate)                    
                i.dx=x_axis_speed
                i.dy=y_axis_speed
                i.radius=radius
                i.shapesize(radius/10)
                i.color(color)
                return False
        

def movearound(event):
    Xcoordinate=event.x-SCREEN_WIDTH
    Ycoordinate=SCREEN_HEIGHT - event.y
    MY_BALL.goto(Xcoordinate,Ycoordinate)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

def printTime():
    #timer function:
    global timer
    turtle.clear()
    turtle.write(timer,font=("Courier",15,"normal"))
    timer=timer-1

def evil_ball_balls():
    for i in BALLS:
        if collide(i,evil_ball)==True:
            i.radius-=1
            i.shapesize(radius/10)

def evil_ball_balls_myball():
    if collide(MY_BALL,evil_ball)==True:
        MY_BALL.radius-=0.5
        MY_BALL.shapesize(MY_BALL.radius/10)



while RUNNING==True and timer>-1:
    global life_counter
    if SCREEN_WIDTH != int(turtle.getcanvas().winfo_width()/2) or SCREEN_HEIGHT!= int(turtle.getcanvas().winfo_height()/2):
        SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2 
        SCREEN_HEIGHT= turtle.getcanvas().winfo_height()/2
    move_all_balls()
    check_all_balls_collision()
    
    if check_myball_collision() ==False:
        print(RUNNING)
        if life_counter ==3:
            print("3)")
            life.hideturtle()
            life_counter=life_counter-1
            RUNNING=True
        elif life_counter==2:
            print("2)")
            life2.hideturtle()
            life_counter=life_counter-1
            RUNNING=True
        elif life_counter==1:
            print("1")
            life3.hideturtle()
            RUNNING=False
    evil_ball_balls_myball()
    evil_ball_balls()
    getscreen().update()
    time.sleep(SLEEP)
    printTime()
if RUNNING==False or timer==-1:
    turtle.clear()
    score=int(MY_BALL.radius)-int(original_radius)
    turtle.write("Time is up, you earned "+str(score)+" points!",align="Center",font=("Courier", 20,"bold"))


turtle.mainloop()
