"""
Animated Sprite (Shifty + Teddy)
by James Paterson.
Working example by Adam Byra

Press the mouse button to change animations.
Demonstrates loading, displaying, and animating GIF images.
It would be easy to write a program to display 
animated GIFs, but would not allow as much control over 
the display sequence and rate of display. 
"""

# From the file "animation.py" import the class "Animation"
from animation import Animation

class Anim():
    def __init__(self):
        self.animation1 = None
        self.animation2 = None
        self.xpos = 0
        self.ypos = 0
        self.drag = 10.0

anim=Anim()
def setup():
    size(1024,768)
    background(255, 204, 0)
    frameRate(24)
    anim.animation1 = Animation("PT_Shifty_", 38)
    anim.animation2 = Animation("PT_Teddy_", 60)

def draw():
    dx = mouseX - anim.xpos
    anim.xpos = anim.xpos + dx / anim.drag
    dy = mouseY - anim.ypos
    anim.ypos = anim.ypos + dy / anim.drag
    # Display the sprite at the position xpos, ypos
    if mousePressed:
        background(153, 153, 0)
        anim.animation1.display(anim.xpos - anim.animation1.getWidth() / 2, anim.ypos)
    else:
        background(255, 204, 0)
        anim.animation2.display(anim.xpos - anim.animation1.getWidth() / 2, anim.ypos)
