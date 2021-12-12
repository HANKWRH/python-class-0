from typing import List
from pycat.core import Window, Sprite, Color
from random import randint, random

from pyglet.image import create
w = Window()


class Particle(Sprite):

    def on_create(self):
        self.time = 0
        self.scale = 5
        self.color = Color.RED
        self.goto_random_position()
        self.rotation = randint(70,110 )
        self.x = w.width/2
        self.y = 0

    def on_update(self, dt):
        self.move_forward(3)
        self.time += dt
        if self.time >= 2:
            self.delete()
            for i in range(10):
                f = w.create_sprite(Firework, x = self.x, y = self.y)


class Firework(Sprite):

    def on_create(self):
        self.rotation = randint(0, 360)
        self.scale = 1
        self.set_random_color()
        self.time = 0
    def on_update(self, dt):
        self.rotation -= 0.5
        self.move_forward(3)
        self.time += dt
        if self.time >= 2:
            self.delete()

class Button(Sprite):

    def on_create(self):
        self.scale = 100
        self.y = 100
        self.x = 100
        self.color = Color.BLUE

    def on_left_click(self):
        for i in range(5):  
            particle.append(w.create_sprite(Particle))
        

blue_button = w.create_sprite(Button)

particle: List[Particle] = []

w.run()