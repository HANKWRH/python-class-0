from typing import List
from pycat.core import Window, Sprite, Color,KeyCode
from random import randint, random

from pyglet.image import create
w = Window()
class Paritcle(Sprite):

    def on_create(self):
        self.time = 0
    def on_update(self, dt):
        self.move_forward(3)
        self.time += dt

class Firework(Paritcle):

    def on_create(self):
        
        super().on_create()
        self.scale = 5
        self.color = Color.RED
        self.goto_random_position()
        self.rotation = randint(70,110 )
        self.x = w.width/2
        self.y = 0

    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.RIGHT):
            self.rotation -= 1
        if w.is_key_pressed(KeyCode.LEFT):
            self.rotation += 1
        super().on_update(dt)
        if self.time >= 2:
            self.delete()
            for i in range(10):
                f = w.create_sprite(Explosion, x = self.x, y = self.y)


class Explosion(Paritcle):

    def on_create(self):
        super().on_create()
        self.rotation = randint(0, 360)
        self.scale = 1
        self.set_random_color()
    def on_update(self, dt):
        self.scale += 0.1
        super().on_update(dt)
        self.rotation -= 0.5
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
            particle.append(w.create_sprite(Firework))
        

blue_button = w.create_sprite(Button)

particle: List[Firework] = []

w.run()