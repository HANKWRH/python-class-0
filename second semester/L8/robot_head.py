from pycat.core import Window, Sprite, Point
from pycat_turtle import Turtle
from random import randint
w = Window(width=1700, enforce_window_limits=False)

t = w.create_sprite(Turtle)


class Rect:
    def __init__(self,x, y, width, height) -> None:
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def draw(self):
        t.x=self.x
        t.y=self.y
        t.rotation=90
        t.draw_line(self.height, 1)
        t.rotation=0
        t.draw_line(self.width, 1)
        t.rotation=270
        t.draw_line(self.height, 1)
        t.rotation=180
        t.draw_line(self.width, 1)
        

class RobotHead:
    def __init__(self, x, y, width, height) -> None:
        self.head = Rect(x, y, width, height)
        self.mouth = Rect(x+0.125*width, y+0.15*height, width*0.75, height*0.35)
        self.lefteye = Rect(x+0.125*width, y+0.65*height, width*0.75*0.25, height*0.15)
        self.righteye = Rect(x+0.125*width+3*width*0.75*0.25, y+0.65*height, width*0.75*0.25, height*0.15)
        self

        

    def draw(self):
        self.head.draw()
        self.mouth.draw()
        self.lefteye.draw()
        self.righteye.draw()


x = 10
width = randint(10, 70)
for i in range(50):
    r=RobotHead(x,100,width,randint(20, 100))
    r.draw()
    x += width+10
    width = randint(10, 50)



w.run()