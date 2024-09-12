# Tash Me with a Click
# 
# Update your Tash Me program ( copy your old program here )to put 
# the moustache where you click on the screen.
#
# Hint: See 08a_More Turtle Programs, section 'Click on the Screen'
 
... # Your code here


import turtle as turtle

turtle.setup(width=600, height=600) 

def set_background_image(window, image_name):
    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

    t = turtle.Turtle()             

screen = turtle.Screen()      
set_background_image(screen, "emoji.png")

def set_turtle_image(turtle, image_name):
    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

set_turtle_image(turtle, "moustache1.gif")

import random

def turtle_clicked(t, x, y):

    print('turtle clicked!')
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    turtle.goto(x, y)
        

turtle.onclick(lambda x, y, t=turtle: turtle_clicked(t, x, y))


turtle.exitonclick()