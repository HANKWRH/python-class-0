from random import random
from pycat.core import Window, Sprite, RotationMode, KeyCode, Point, Scheduler
from enum import Enum, auto
from random import randint


w = Window(is_sharp_pixel_scaling=True)

Y_MIN = 100
Y_MAX = 540
SCALE_MIN = 45
SCALE_MAX = 60
S_D = SCALE_MAX - SCALE_MIN
D = 50
ATK_DMG = 5
def get_scale(y):
    a = (Y_MAX - y)/(Y_MAX - Y_MIN)
    return SCALE_MIN+a*S_D


def spwan_enemy(dt):
    w.create_sprite(Enemy)


Scheduler.update(spwan_enemy, 2)


class Enemy(Sprite):
    total_enemies = 0

    class State(Enum):
        WAIT = auto()
        CHASE = auto()
        DIE = auto()

    def on_create(self):
        Enemy.total_enemies += 1
        if Enemy.total_enemies > 3:
            Scheduler.cancel_update(spwan_enemy)
        self.add_tag('enemy')
        self.y = 0
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.scale = 1
        self.time = 0
        self.x = w.width/2
        self.y = w.height/2
        self.image = 'img/Wait.PNG'
        self.state = Enemy.State.WAIT
        self.healthbar = w.create_sprite(Healthbar)
        self.hp = 100
        self.is_attacking = False
        self.attacktime = 0
        self.goto_random_position()

    def delete():
        super().delete()
        Enemy.total_enemies -= 1
        if Enemy.total_enemies < 3:
            Scheduler.update(spwan_enemy, 2)


    def on_update(self, dt):
        if self.is_attacking:
            self.attacktime += dt
            if self.attacktime >= 2:
                self.attacktime = 0
                self.is_attacking = False
        elif self.is_touching_sprite(player):
            self.is_attacking = True
            player.hp-= ATK_DMG
            player.healthbar.set_width(player.hp/100)
        self.scale = get_scale(self.y)*0.02
        self.time += dt
        self.healthbar.position = self.position
        self.healthbar.y += self.height/2+5
        if self.time >= 1.5:
            self.state = Enemy.State.CHASE
        if self.state == Enemy.State.CHASE:
            self.point_toward_sprite(player)
            self.move_forward(D)
            self.state = Enemy.State.WAIT
            self.time = 0
        
        sword = self.get_touching_sprites_with_tag('attack')
        if sword:
            self.hp -= ATK_DMG
            self.healthbar.set_width(self.hp/100)
            sword[0].remove_tag("attack")
        
        
        
    
    def jump(self, dt):
        # if self.scale_x <= 0.5 and self.time >= 0.5:
        #     self.scale_x += 0.01
            
        # if self.time :
        #     self.scale_x -= 0.01
        #     self.time = 0
        pass


class Healthbar(Sprite):
    def on_create(self):
        self.scale_x = 100
    
    def set_width(self, v: float):
        self.scale_x = 100*v


    # def on_update(self, dt):
    #     self.position = enemy.position
    #     self.y = enemy.y + 40

class Player(Sprite):
    class State(Enum):
        WAIT = auto()
        BE_ATK = auto()
        DIE = auto()

    def on_create(self):
        self.state = self.State.WAIT
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.scale = 100
        self.x = 0
        self.y = w.height/2
        self.move_dir = Point(0,0)
        self.healthbar = w.create_sprite(Healthbar)
        self.hp = 100
    def on_update(self, dt):
        self.healthbar.position = self.position
        self.healthbar.y += self.height/2+5
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
        if w.is_key_down(KeyCode.N):
            w.create_sprite(Sword)
        
        


class Sword(Sprite):
    def on_create(self):
        self.rotation = -30
        self.scale = 0.5
        self.position = player.position
        self.x += player.width/2 + 10
        self.image = 'img/sword.png'
        self.add_tag('attack')
    def on_update(self, dt):
        self.rotation -= 5
        if self.rotation <= -120:
            self.delete()


enemy = w.create_sprite(Enemy)
player = w.create_sprite(Player)

w.run()