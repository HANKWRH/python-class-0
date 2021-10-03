from pycat.core import Window,  KeyCode, Sprite, RotationMode, Color
from random import randint

w = Window()

class Owl(Sprite):

    def on_create(self):
        self.image = "img/owl.png"
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.health = 5
        self.speed = 5
        
    def on_update(self, dt):
        self.move_forward(self.speed)
        if w.is_key_pressed(KeyCode.RIGHT):
            self.rotation = 0
        if w.is_key_pressed(KeyCode.UP):
            self.rotation = 90
        if w.is_key_pressed(KeyCode.LEFT):
            self.rotation = 180
        if w.is_key_pressed(KeyCode.DOWN):
            self.rotation = 270
        # if self.is_touching_any_sprite():
        #     self.health -= 1
        #     print(self.health)
        #     self.color = Color.RED
        # else:
        #     self.color = Color.WHITE
        if self.health <= 0:
            print('you lose')
            w.close()
        if self.x >= 1280:
            print('you win')
            w.close()


owl = w.create_sprite(Owl)

class Ghost(Sprite):
    def on_create(self):
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.rotation = 180
        self.scale = 0.3
        self.x = 1280
        self.y = randint(0, w.height)
        self.image='img/ghost.png'
    def on_update(self, dt):
        self.x -= 8
        if self.x <= 0:
            self.goto_random_position()
            self.x = 1280
        
        elif self.is_touching_sprite(owl):
            self.goto_random_position()
            self.x = 1280
            owl.health -= 1
            owl.color = Color.RED
        else:
            owl.color = Color.WHITE

        if self.is_touching_any_sprite():
            self.goto_random_position()
            self.x = 1280

class Star(Sprite):
    def on_create(self):
        self.image = 'img/star.png'
        self.goto_random_position()
    def on_update(self, dt):
        if self.is_touching_sprite(owl):
            self.delete()
            owl.speed +=10



w.create_sprite(Ghost)
w.create_sprite(Ghost)
w.create_sprite(Ghost)    
w.create_sprite(Ghost)
w.create_sprite(Star)

w.run()
