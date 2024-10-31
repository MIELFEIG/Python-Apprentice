"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed(50)

def drawTreeSegment(treeWidth):
    tina.pendown()
    tina.setheading(90)
    tina.begin_fill()
    tina.fillcolor('#0bb839')
    tina.forward(200)
    tina.right(90)
    tina.forward(treeWidth)
    tina.right(90)
    tina.forward(200)
    tina.right(90)
    tina.forward(treeWidth)
    tina.end_fill()
    tina.penup()

def drawTree(treeWidth,numSegments):
    for i in range(numSegments):
        drawTreeSegment(40)
        tina.setheading(90)
        tina.forward(200)


def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

draw_circle('white',100,0,-140)
draw_circle('white',75,0,20)
draw_circle('black',15,-35,100)
draw_circle('white',5,-35,100)
draw_circle('black',15,35,100)
draw_circle('white',5,35,100)
draw_circle('black',20,-50,140)
draw_circle('black',20,50,140)
draw_circle('black',10,0,50)

tina.penup()
tina.goto(-10,40)
tina.pendown()
tina.setheading(270)
tina.circle(radius = 10, extent= 180, steps= 20)

draw_circle('black',35,-90,-30)
draw_circle('black',35,90,-30)
draw_circle('black',35,90,-140)
draw_circle('black',35,-90,-140)


tina.penup()
tina.goto(-300,-250)

drawTree(40,3)

tina.goto(150,-250)

drawTree(40,3)

tina.goto(-250,-250)

drawTree(50,2)

tina.goto(200,-250)

drawTree(40,2)

tina.goto(250,-250)

drawTree(50,3)

tina.goto(-200,-250)

drawTree(50,1)






turtle.exitonclick()                    # Close the window when we click on it
