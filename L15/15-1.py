from pycat.core import Color, KeyCode, Sprite, Window
from random import randint

from pycat.label import Label
w = Window()
class Lose(Label):
    def on_create(self):
        self.x = 540
        self.y = 340
    def on_update(self, dt: float):
        if player.health.width <= 0:
            w.delete_all_sprites()
            self.text = 'Loooooose'

w.create_label(Lose) 

class Win(Label):
    def on_create(self):
        self.x = 540
        self.y = 340
    def on_update(self, dt: float):
        if player.x >= 1280 and player.y >= 150:
            w.delete_all_sprites()
            self.text = 'You Win'
w.create_label(Win)



class HealthBar(Sprite):
    def on_create(self):
        self.color = Color.RED
        self.width = 50
        self.height = 2
        self.dx = 0
    def on_update(self, dt):
        pass

class Player(Sprite):
    def on_create(self):
        self.health = w.create_sprite(HealthBar)
        self.is_touching_ground = False
        self.y = 200
        self.scale = 15
        self.y_speed = 0
        self.layer = 2
        self.btime = 0
        self.ntime = 0
    def on_update(self, dt):
        self.btime += dt
        self.ntime += dt
        if self.is_touching_sprite(dp):
            self.health.width -= 10
            self.health.dx -= 5
            self.x = 10
            self.y = 20
        if self.is_touching_any_sprite_with_tag('eb'):
            for b in self.get_touching_sprites_with_tag('eb'):
                b.delete()
            self.health.width -= 5
            self.health.dx -= 2.5
        if self.health.width <= 0:
            self.delete()
        x = self.x
        if w.is_key_pressed(KeyCode.D):
            self.rotation = 0
            self.move_forward(5)
        if w.is_key_pressed(KeyCode.A):
            self.rotation = 180
            self.move_forward(5)
        if w.is_key_down(KeyCode.W):
            if self.is_touching_ground:
                self.y_speed = 10
                self.is_touching_ground = False
        if self.rotation == 0 and self.is_touching_any_sprite_with_tag('platform'):
            self.move_forward(-5)
        if self.rotation == 180 and self.is_touching_any_sprite_with_tag('platform'):
            self.move_forward(-5)
        self.y += self.y_speed
        self.y_speed -= 0.5
        if self.y_speed < 0:
            while self.is_touching_any_sprite_with_tag('platform'):
                
                self.is_touching_ground = True
                self.y_speed = 0
                self.y += 0.5
        if w.is_key_down(KeyCode.B):
            if self.btime >= 0.5:
                w.create_sprite(PlayerBullet)
                self.btime = 0
        if w.is_key_down(KeyCode.N):
            if self.ntime >= 3:    
                w.create_sprite(Pb2)
                self.ntime = 0

        self.health.x = self.x + self.health.dx
        self.health.y = self.y + 20
        


player = w.create_sprite(Player)

class PlayerBullet(Sprite):
    def on_create(self):
        self.scale = 3
        self.goto(player)
        self.add_tag('pb')
        self.rotation = player.rotation
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()
        


class PlatformDie(Sprite):
    def on_create(self):
        self.scale = 100
        self.scale_x = 10
        self.color = Color.BLUE
        self.x = 700
        self.y = 40
        self.time = 0
    def on_update(self, dt):
        if enemy.is_deleted == True:
            if 'platform' not in self.tags:
                self.color = Color.AMBER
                self.add_tag('platform')



class Platform(Sprite):
    def on_create(self):
        self.scale = 100
        self.scale_x = 4
        self.x = 200
        self.color = Color.AMBER
        self.add_tag('platform')
        self.layer = 2
    def on_update(self, dt):
        pass


class Enemy(Sprite):
    def on_create(self):
        self.timech = 0
        self.color = Color.MAGENTA
        self.health = w.create_sprite(EnemyHealth)
        self.scale = 70
        self.x = 1100
        self.y = 450
        self.y_speed = 0
        self.is_touching_ground = False
        self.time = 0
        self.rotation = 180
    def on_update(self, dt):
        self.timech += dt
        if self.timech >= 10 and self.timech <= 10.10:
            self.y = 150
        elif self.timech >= 20:
            self.y = 450
            self.timech = 0
        if self.is_touching_any_sprite_with_tag('pb'):
            for b in self.get_touching_sprites_with_tag('pb'):
                b.delete()
            self.health.width -= 5
            self.health.dx -= 2.5
        self.health.x = self.x + self.health.dx
        self.health.y = self.y + 40
        self.time += dt
        self.y += self.y_speed
        self.y_speed -= 0.5
        if self.health.width <= 0:
            self.delete()
        # if not self.is_touching_ground:
        #     self.move_forward(5)
        if self.y_speed < 0:
            
            while self.is_touching_any_sprite_with_tag('platform'):
                self.is_touching_ground = True
                
                self.y_speed = 0
                self.y += 1
        if self.time >= 3:
            if self.rotation == 0:
                self.rotation = 180
            else:
                self.rotation = 0
            if self.is_touching_ground:
                self.y_speed = 8
                self.is_touching_ground = False
                b = w.create_sprite(EnemyBullet)
                b.position = self.position
                b.point_toward_sprite(player)
            self.time = 0
        

class EnemyBullet(Sprite):
    def on_create(self):
        self.color = Color.VIOLET
        self.scale = 10
        self.add_tag('eb')
    def on_update(self, dt):
        self.move_forward(20)
        if self.is_touching_window_edge():
            self.delete()
        # if self.is_touching_sprite(player):
        #     if health.width > 5:
        #         health.width -= 5
        #         health.dx -= 2.5
        #     self.delete()


class Storm(Sprite):
    def on_create(self):
        self.add_tag('storm')
        self.x = randint(0, 1250)
    def on_update(self, dt):
        self.y -= 1
        if self.is_touching_any_sprite_with_tag('platform'):
            self.delete()


class EnemyHealth(Sprite):
    def on_create(self):
        self.color = Color.RED
        self.width = 150
        self.height = 2
        self.dx = 0
    def on_update(self, dt):
        pass


class Pb2(Sprite):
    def on_create(self):
        
        self.time = 0
        
        self.y_speed = 8
        self.x_speed = 20
        self.color = Color.TEAL
        self.scale = 5
        self.goto(player)
        if player.rotation == 180:
            self.x_speed *= -1
    def on_update(self, dt):
        self.time += dt
        self.y += self.y_speed
        self.y_speed -= 0.5
        self.x += self.x_speed
        if self.y_speed < 0:
            while self.is_touching_any_sprite_with_tag('platform'):
                self.y += 0.5
                self.x_speed = 0
                self.y_speed = 0
        if self.time >= 3:
            self.delete()
            for i in range(5):
                w.create_sprite(Explosion, position=self.position)
        

class Door(Sprite):
    def on_create(self):
        self.scale = 10

        self.scale_y = 5
        self.x = 1200
        self.y = 140
    def on_update(self, dt):
        if enemy.is_deleted:
            self.y-=1
        pass
w.create_sprite(Door)


class Explosion(Sprite):
    def on_create(self):
        self.image = 'smoke.png'
        self.scale = 0.1
        self.add_tag('pb')
        self.opacity = 50
        self.time = 0
        self.rotation = randint(0,360)
    def on_update(self, dt):
        self.time += dt
        self.move_forward(2)
        if self.time >= 0.5:
            self.delete()


w.create_sprite(Platform)
p = w.create_sprite(Platform, x = 300, y = 150)
p.width = 200
p.height = 10
dp = w.create_sprite(PlatformDie)
dp.width = 600
dp.height = 10
q = w.create_sprite(Platform, x = 1200, y = 100)
q.width = 400
q.height = 40
r = w.create_sprite(Platform, x = 0, y = 250)
r.width = 200
r.height = 10
s = w.create_sprite(Platform, x = 300, y = 350)
s.width = 200
s.height = 10
t = w.create_sprite(Platform, x = 1100, y = 350)
t.width = 400
t.height = 40
u = w.create_sprite(Platform, x = 1200, y = 40)
v = w.create_sprite(Platform, x = 1240, y = 160)
v.height = 10
v.width = 100
w.create_sprite(Enemy)
w.create_sprite(Player)
# w.create_sprite(PlatformDie)
enemy = w.create_sprite(Enemy)
w.run()
                                                                           
