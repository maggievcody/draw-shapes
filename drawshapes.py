# Draw Shapes:
# Takes in input of shape and color in lowercase letters and returns
# the shape filled with that color using turtle graphics.
def DrawShapes():
	import turtle
	userinput = input('What shape would you like? (square, triangle, circle) ')
	filled = input('What color would you like? (red, blue, green, purple, orange, yellow) ')
	myturtle = turtle.Turtle()
	screen = turtle.Screen()
	if userinput == 'square':
		myturtle.goto(0,0)
		myturtle.fillcolor(filled)
		myturtle.color(filled)
		myturtle.pendown()
		myturtle.begin_fill()
		myturtle.forward(100)
		myturtle.right(90)
		myturtle.forward(100)
		myturtle.right(90)
		myturtle.forward(100)
		myturtle.right(90)
		myturtle.forward(100)
		myturtle.end_fill()
		screen.delay(15)
	elif userinput == 'triangle':
		myturtle.goto(0,0)
		myturtle.fillcolor(filled)
		myturtle.color(filled)
		myturtle.pendown()
		myturtle.begin_fill()
		myturtle.forward(100)
		myturtle.left(120)
		myturtle.forward(100)
		myturtle.left(120)
		myturtle.forward(100)
		myturtle.end_fill()
		screen.delay(15)
	elif userinput == 'circle':
		myturtle.fillcolor(filled)
		myturtle.color(filled)
		myturtle.goto(0,0)
		myturtle.pendown()
		myturtle.begin_fill()
		myturtle.circle(100)
		myturtle.end_fill()
		screen.delay(15)
	else:
		'Sorry, we did not understand your input. Please try again.'

#print(DrawShapes())
