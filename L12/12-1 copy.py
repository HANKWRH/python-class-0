from typing import List
from pycat.core import Window, Sprite, Color
from random import randint, random

from pyglet.image import create
w = Window()
def get_random_speed(low, high):
    is_nagetive = randint(0, 1)
    speed = low + random()*high
    if is_nagetive == 1:
        speed = -speed
    return speed


class Particle(Sprite):

    def on_create(self):
        self.scale = 5
        self.color = Color.RED
        self.goto_random_position()
        self.rotation = randint(1,360 )
        
        self.x_speed = get_random_speed(1,2)
        self.y_speed = get_random_speed(1,2)

    def on_update(self, dt):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.y < 0 or self.y > w.height:
            self.y_speed = -self.y_speed
        if self.x < 0 or self.x > w.width:
            self.x_speed = -self.x_speed


class Button(Sprite):

    def on_create(self):
        self.scale = 100
        self.y = 100

    def on_left_click(self):
        if self.color == Color.RED:
            
            for p in particle:
                p.delete()
                p.color = Color.RED
            particle.clear()
        if self.color == Color.BLUE:
            for i in range(10):  
                particle.append(w.create_sprite(Particle))
            for p in particle:
                p.color = Color.BLUE
        
red_button = w.create_sprite(Button)
red_button.x = 100
red_button.color = Color.RED
blue_button = w.create_sprite(Button)
blue_button.x = 200
blue_button.color = Color.BLUE
particle: List[Particle] = []

w.run()