import turtle
turtle.speed(100)
turtle.pensize(10)


angle  = 20
for i in range(18):
	turtle.left(angle)
	for i in range(4):
		turtle.forward(120)
		turtle.left(90)

turtle.mainloop()
