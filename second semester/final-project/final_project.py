from pycat.core import Window, Sprite, RotationMode, KeyCode, Point
from enum import Enum, auto


w = Window(is_sharp_pixel_scaling=True)

class Enemy(Sprite):

    class State(Enum):
        CHASE = auto()
        DIE = auto()

    def on_create(self):
        self.add_tag('enemy')
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.scale = 1
        self.time = 0
        self.x = w.width/2
        self.y = w.height/2
        self.image = 'img/Wait.PNG'
        self.state = Enemy.State.CHASE


    def on_update(self, dt):
        self.time += dt
        self.move_forward(1)
        self.point_toward_sprite(player)
        
        
    
    def jump(self, dt):
        # if self.scale_x <= 0.5 and self.time >= 0.5:
        #     self.scale_x += 0.01
            
        # if self.time :
        #     self.scale_x -= 0.01
        #     self.time = 0
        pass

class Player(Sprite):
    def on_create(self):
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.scale = 100
        self.x = w.width/2
        self.y = w.height/2
        self.move_dir = Point(0,0)
    def on_update(self, dt):
        self.point_toward_sprite(enemy)
        self.move_dir = Point(0,0)
        if w.is_key_pressed(KeyCode.A):
            self.move_dir += Point(-1,0)
        if w.is_key_pressed(KeyCode.D):
            self.move_dir += Point(1,0)
        if w.is_key_pressed(KeyCode.S):
            self.move_dir += Point(0,-1)
        if w.is_key_pressed(KeyCode.W):
            self.move_dir += Point(0,1)
        if w.is_key_pressed(KeyCode.SPACE):
            self.move_dir *= 5
        else:
            self.move_dir *= 2
        self.position += self.move_dir

enemy = w.create_sprite(Enemy)
player = w.create_sprite(Player)
w.run()