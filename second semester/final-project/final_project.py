from cProfile import label
from pycat.core import Window, Sprite, RotationMode, KeyCode, Point, Scheduler, Label
from enum import Enum, auto
from random import randint


w = Window(enforce_window_limits=False, is_sharp_pixel_scaling=True)

Y_MIN = 100
Y_MAX = 540
SCALE_MIN = 45
SCALE_MAX = 60
STAGE_Y0 = 100
STAGE_Y1 = w.height - 100
S_D = SCALE_MAX - SCALE_MIN
X1 = 100
X2 = w.width-100
D = 50

ATK_DMG = 50
def get_scale(y):
    a = (Y_MAX - y)/(Y_MAX - Y_MIN)
    return SCALE_MIN+a*S_D

r = get_scale(STAGE_Y1)/get_scale(STAGE_Y0)
L = X2-X1
L2 = r*L
x1 = w.center.x - (L2/2)
x2 = w.center.x + (L2/2)
w.create_line(X1, STAGE_Y0, X2, STAGE_Y0)
w.create_line(x1, STAGE_Y1, x2, STAGE_Y1)
w.create_line(X1, STAGE_Y0, x1, STAGE_Y1)
w.create_line(X2, STAGE_Y0, x2, STAGE_Y1)
w.create_line(X1, 20, X2, 20)
w.create_line(X1, STAGE_Y0, X1, 20)
w.create_line(X2, STAGE_Y0, X2, 20)
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
        self.goto_random_position()
        self.image = 'img/Wait.PNG'
        self.state = Enemy.State.WAIT
        self.healthbar = w.create_sprite(Healthbar)
        self.set_health()
        self.hp = 100
        self.is_attacking = False
        self.attacktime = 0
        

    def set_health(self):
        self.healthbar.position = self.position
        self.healthbar.y += self.height/2+5

    def delete(self):
        super().delete()
        self.healthbar.delete()
        Enemy.total_enemies -= 1
        if Enemy.total_enemies < 3:
            Scheduler.update(spwan_enemy, 2)


    def on_update(self, dt):
        self.layer = -self.y
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
        self.set_health()
        if self.time >= 1.5:
            self.state = Enemy.State.CHASE
        if self.state == Enemy.State.CHASE:
            self.point_toward_sprite(player)
            self.move_forward(D)
            self.state = Enemy.State.WAIT
            self.time = 0
            self.set_health()
        sword = self.get_touching_sprites_with_tag('attack')
        if sword:
            self.hp -= ATK_DMG
            self.healthbar.set_width(self.hp/100)
            sword[0].remove_tag("attack")
        if self.hp <= 0:
            self.state = Enemy.State.DIE
        if self.state == Enemy.State.DIE:
            self.delete()
            player.kills += 1
            
            
        
        
        
        
    
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
        self.kills = 0
        self.state = self.State.WAIT
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.scale = 100
        self.x = 0
        self.y = w.height/2
        self.move_dir = Point(0,0)
        self.healthbar = w.create_sprite(Healthbar)
        self.hp = 100
    def on_update(self, dt):
        self.layer = -self.y
        self.healthbar.position = self.position
        self.healthbar.y += self.height/2+5
        self.scale = get_scale(self.y)
        self.move_dir = Point(0,0)
        if w.is_key_pressed(KeyCode.A):
            self.rotation = 180
            self.move_dir += Point(-1,0)
        if w.is_key_pressed(KeyCode.D):
            self.rotation = 0
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
        if self.hp <= 0:
            w.delete_all_sprites()
            Scheduler.cancel_update(spwan_enemy)
            w.create_label(Lose)
        if self.kills >= 5:
            w.delete_all_sprites()
            
            Scheduler.cancel_update(spwan_enemy)
            w.create_label(Win)



class Sword(Sprite):
    def on_create(self):
        self.time = 0
        self.position = player.position
        # self.x += player.width/2 + 10
        # self.y = player.y
        self.image = 'img/sword.png'
        self.add_tag('attack')
        self.rotation = player.rotation
        print(self.rotation)
    def on_update(self, dt):
        self.time += dt
        # self.position = player.position
        self.move_forward(10)
        if self.time >= 0.25:
            self.delete()

class Win(Label):
    def on_create(self):
        self.x = w.width/2
        self.y = w.height/2
        self.font_size = 50
    def on_update(self, dt: float):
        self.text = 'Win'


class Lose(Label):
    def on_create(self):
        self.x = w.width/2
        self.y = w.height/2
        self.font_size = 50
    def on_update(self, dt: float):
        self.text = 'Lose'
enemy = w.create_sprite(Enemy)
player = w.create_sprite(Player)

w.run()