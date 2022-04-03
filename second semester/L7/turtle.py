from pycat.core import Window, Sprite, Point
w = Window()


class Turtle(Sprite):
    def draw_line(self, distance:int, width:int = 1):
        a = self.position
        super().move_forward(distance)
        b = self.position
        w.create_line(a.x, a.y, b.x, b.y)
    def draw_triangle(self, distance):
        for j in range(3):
            for i in range(36):
                for _ in range(3):
                    self.draw_line(distance)
                    self.rotation += 120
                self.rotation += 10
            self.rotation += 120
            self.move_forward(distance)
    def draw_regular_polygon(self, sides, distance):
        a = 360 / sides
        for _ in range(sides):
            self.draw_line(distance)
            self.rotation += a
    


t = w.create_sprite(Turtle)
t.position = w.center
# for j in range(6):
#     for i in range(3, 10):
#         t.draw_regular_polygon(i, 70)
#     t.rotation += 90
t.draw_triangle(100)



w.run()