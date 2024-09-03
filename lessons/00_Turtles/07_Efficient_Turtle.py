
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):

    angle = 360/sides
    side_length = 50 # Calculate angle from number of sides
    
    for i in range(sides):   
        tina.forward(side_length) 
        tina.left(angle)             # Loop through the number of sides
                                # Move tina forward by the forward distance
                                     # Turn tina left by the left turn


draw_polygon(4)    
              # Draw a square
tina.penup()
tina.goto(50, -100)
tina.pendown()
                                     # Move tina to another spot on the screen

draw_polygon(5)   

tina.penup()
tina.goto(-100, 150)
tina.pendown()
               # Draw a pentagon

                                    # Move tina to another spot on the screen

draw_polygon(6)


                      # Draw a hexagon


turtle.exitonclick()                     # Close the window when we click on it
