
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

... # Your code here

import turtle as turtle

screen = turtle.Screen()  
screen.setup(width=600, height=600)  


#t.turtlesize(stretch_wid=10, stretch_len=10, outline=4)


def set_background_image(window, image_name):
    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)          

def set_turtle_image(turtle, image_name,screen):
    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    #screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

def turtle_clicked(t, x, y):

    print('turtle clicked!')
    
    #for i in range(0,10):
    t.left(20)



t = turtle.Turtle()   
set_turtle_image(t, "moustache1.gif", screen)
set_background_image(screen, "emoji.png")
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.done()