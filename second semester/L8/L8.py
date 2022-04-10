from pycat.core import Window, Sprite, Point
from pycat_turtle import Turtle
w = Window()



    


t = w.create_sprite(Turtle)
t.position = w.center
# for j in range(6):
#     for i in range(3, 10):
#         t.draw_regular_polygon(i, 70)
#     t.rotation += 90
t.draw_triangle(100)



w.run()