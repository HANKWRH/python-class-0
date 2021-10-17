from pycat.core import Window, Sprite, RotationMode, Scheduler
from random import randint
from pycat.keyboard import KeyCode
w = Window(background_image="img/beach_03.png")
class Player(Sprite):
    def on_create(self):
        self.image='img/cat.png'
        self.x = 50
        self.y = 50
        self.score = 0
    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.LEFT):
            self.scale_x = -1
            self.x -= 10
        if w.is_key_pressed(KeyCode.RIGHT):
            self.x += 10
            self.scale_x = 1
        # if self.is_touching_any_sprite_with_tag("gem"):
        #     print(self.score)
        if self.x == 1280:
            self.x -= 10
class Gem(Sprite):
    def on_create(self):
        self.image = 'img/gem01.png'
        self.scale = 0.3
        self.y = 1080
        self.x = randint(0, w.width)
        self.add_tag("gem")
    def on_update(self, dt):
        self.y -= 5
        if self.y <= 0:
            self.delete()
        elif self.is_touching_sprite(player):
        #     player.score += 1
            self.delete()
            


def create_gem():
    w.create_sprite(Gem)

Scheduler.update(create_gem, 0.5)
player = w.create_sprite(Player)
w.run()