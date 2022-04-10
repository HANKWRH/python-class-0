from pycat.core import Sprite

class Turtle(Sprite):
    def draw_line(self, distance:int, width:int = 1):
        a = self.position
        super().move_forward(distance)
        b = self.position
        self.window.create_line(a.x, a.y, b.x, b.y)
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