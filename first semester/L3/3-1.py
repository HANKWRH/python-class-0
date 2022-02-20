
from pycat.core import Window, KeyCode
from pycat.sprite import Sprite
from pyglet import window
w = Window()


class Fireball(Sprite):

    def on_create(self):
        self.image = "fireball.gif"
        self.x = 0
        self.y = 300
    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.BACKSPACE):
            self.x += 3
        elif w.is_key_pressed(KeyCode.SPACE) and w.is_key_pressed(KeyCode.ENTER):
            self.x += 5
class Fireball(Sprite):

    def on_create(self):
        self.image = "fireball.gif"
        self.x = 0
        self.y = 300
    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.BACKSPACE):
            self.x += 3
        elif w.is_key_pressed(KeyCode.SPACE) and w.is_key_pressed(KeyCode.ENTER):
            self.x += 5
w.create_sprite(Fireball)
w.create_sprite(Fireball)

w.run()