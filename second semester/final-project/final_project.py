from turtle import position
from pycat.core import Window, Sprite, RotationMode, KeyCode, Point
from enum import Enum, auto



w = Window(is_sharp_pixel_scaling=True)

Y_MIN = 100
Y_MAX = 540
SCALE_MIN = 45
SCALE_MAX = 60
S_D = SCALE_MAX - SCALE_MIN
D = 50

def get_scale(y):
    a = (Y_MAX - y)/(Y_MAX - Y_MIN)
    return SCALE_MIN+a*S_D


class Enemy(Sprite):

    class State(Enum):
        WAIT = auto()
        CHASE = auto()
        DIE = auto()

    def on_create(self):
        self.add_tag('enemy')
        self.y = 0
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.scale = 1
        self.time = 0
        self.x = w.width/2
        self.y = w.height/2
        self.image = 'img/Wait.PNG'
        self.state = Enemy.State.WAIT


    def on_update(self, dt):
        self.scale = get_scale(self.y)*0.02
        self.time += dt
        if self.time >= 1.5:
            self.state = Enemy.State.CHASE
        if self.state == Enemy.State.CHASE:
            self.point_toward_sprite(player)
            self.move_forward(D)
            self.state = Enemy.State.WAIT
            self.time = 0
        
        
        
    
    def jump(self, dt):
        # if self.scale_x <= 0.5 and self.time >= 0.5:
        #     self.scale_x += 0.01
            
        # if self.time :
        #     self.scale_x -= 0.01
        #     self.time = 0
        pass


class E_healthbar(Sprite):
    def on_create(self):
        self.scale_x = 100

    def on_update(self, dt):
        self.position = enemy.position
        self.y = enemy.y + 40

class Player(Sprite):
    def on_create(self):
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.scale = 100
        self.x = w.width/2
        self.y = w.height/2
        self.move_dir = Point(0,0)
    def on_update(self, dt):
        self.scale = get_scale(self.y)
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
            self.move_dir *= 1
        self.position += self.move_dir
        if w.is_key_pressed(KeyCode.N):
            w.create_sprite(Sword)


class Sword(Sprite):
    def on_create(self):
        self.scale = 0.5
        self.position = player.position
        self.image = 'img/sword.png'
    def on_update(self, dt):
        self.rotation -= 2
        if self.rotation <= -30:
            self.delete()


enemy = w.create_sprite(Enemy)
player = w.create_sprite(Player)
e_healthbar = w.create_sprite(E_healthbar)
w.run()