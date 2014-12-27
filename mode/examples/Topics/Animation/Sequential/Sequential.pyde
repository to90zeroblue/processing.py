"""
Sequential
by James Paterson.
Variable scope, minor edits, by Adam Byra.

Displaying a sequence of images creates the illusion of motion. 
Twelve images are loaded and each is displayed individually in a loop. 
"""

class Anim():
    def __init__(self):
        self.numFrames = 12
        self.currentFrame = 0
        self.images = [PImage] * self.numFrames
        self.animWidth=0

    def loadGraphic(self):
        txtHead='PT_anim0000'
        txtTail='.gif'
        for i in range(self.numFrames):
            txtCombined=txtHead[:-(i/10+1)]+str(i)+txtTail
            self.images[i]=loadImage(txtCombined)
            
anim=Anim()
def setup():
    size(640, 360)
    frameRate(24)
    anim.loadGraphic()
    anim.animWidth=anim.images[0].width
    
def draw():
    background(0)
    # Use % to cycle through frames
    anim.currentFrame = (anim.currentFrame + 1) % anim.numFrames
    offset = 0
    for x in range(-100, width, anim.animWidth):
        image(anim.images[(anim.currentFrame + offset) % anim.numFrames], x, -20)
        offset += 2
        image(anim.images[(anim.currentFrame + offset) % anim.numFrames], x, height / 2)
        offset += 2
        
