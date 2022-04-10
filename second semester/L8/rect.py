from pycat.core import Window, Sprite, Point
from pycat_turtle import Turtle
w = Window()

t = w.create_sprite(Turtle)
t.rotation=45
t.draw_line(200)

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

r=Rect(0,0,100,100)
r.draw()



w.run()


