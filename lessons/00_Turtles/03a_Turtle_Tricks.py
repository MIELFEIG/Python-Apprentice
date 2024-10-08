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


def drawTree(treeWidth,numSegments):
    tina.pencolor('green')
    tina.pendown()
    tina.left(90)
    tina.forward(200)
    tina.right(90)
    tina.forward(treeWidth)
    tina.right(90)
    tina.forward(200)
    tina.left(180)
    tina.forward(400)
    tina.left(90)
    tina.forward(treeWidth)
    tina.left(90)
    tina.forward(400)
    tina.penup()

tina.penup()
tina.goto(-200,-250)

drawTree(40)



tina.goto(-250, -250)
tina.pencolor('green')
tina.pendown()
tina.left(180)
tina.forward(200)
tina.left(90)
tina.forward(40)
tina.left(90)
tina.forward(200)
tina.left(180)
tina.forward(400)
tina.right(90)
tina.forward(40)
tina.right(90)
tina.forward(400)
tina.left(180)
tina.forward(500)
tina.left(90)
tina.forward(40)
tina.left(90)
tina.forward(200)

tina.penup()
tina.pencolor('black')
tina.goto(0,100)

tina.circle(50)





turtle.exitonclick()                    # Close the window when we click on it
