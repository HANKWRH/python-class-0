from pycat.core import Window, Point
from random import randint
w = Window()

def get_randint_point():
    x = randint(0, w.width)
    y = randint(0, w.height)
    return Point(x,y)

def draw_random_triangle(line_width: int = 1):
    a = get_randint_point()
    b = get_randint_point()
    c = get_randint_point()
    w.create_line(a.x, a.y, b.x, b.y, line_width)
    w.create_line(b.x, b.y, c.x, c.y, line_width)
    w.create_line(c.x, c.y, a.x, a.y, line_width)

# draw_random_triangle(8)

def draw_triangle(a: Point, b: Point, c: Point, line_width: int = 1):
    w.create_line(a.x, a.y, b.x, b.y, line_width)
    w.create_line(b.x, b.y, c.x, c.y, line_width)
    w.create_line(c.x, c.y, a.x, a.y, line_width)

a = get_randint_point()
b = get_randint_point()
c = get_randint_point()
# draw_triangle(a, b, c, 1)

def draw_subdivisions_triangle(subdivisions: int, a: Point, b: Point, c: Point, w: int = 1):
    if subdivisions <= 0:
        draw_triangle(a, b, c, w)
    else:
        d = (a+b) / 2
        e = (b+c) / 2
        f = (a+c) / 2
        n = subdivisions - 1
        draw_subdivisions_triangle(n, d, e, f, w)
        draw_subdivisions_triangle(n, a, d, f, w)
        draw_subdivisions_triangle(n, c, e, f, w)
        draw_subdivisions_triangle(n, b, d, e, w)
draw_subdivisions_triangle(3, a, b, c, 3)
w.run()
