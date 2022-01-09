from pycat.core import Color, KeyCode, Sprite, Window
from random import randint

from pycat.label import Label
w = Window()
class Lose(Label):
    def on_create(self):
        self.x = 540
        self.y = 340
    def on_update(self, dt: float):
        if player.is_deleted == True:
            w.delete_all_sprites()
            self.text = 'Loooooose'

w.create_label(Lose)       




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
        
    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag('eb'):
            for b in self.get_touching_sprites_with_tag('eb'):
                b.delete()
            self.health.width -= 5
            self.health.dx -= 2.5
        if self.health.width <= 0:
            self.delete()
        if w.is_key_pressed(KeyCode.D):
            self.rotation = 0
            self.move_forward(5)
        if w.is_key_pressed(KeyCode.A):
            self.rotation = 180
            self.move_forward(5)
        if w.is_key_down(KeyCode.W):
            if self.is_touching_ground:
                self.y_speed = 8
                self.is_touching_ground = False
        self.y += self.y_speed
        self.y_speed -= 0.5
        if self.y_speed < 0:
            while self.is_touching_any_sprite_with_tag('platform'):
                self.is_touching_ground = True
                self.y_speed = 0
                self.y += 0.5
        if w.is_key_down(KeyCode.B):
            w.create_sprite(PlayerBullet)
        if w.is_key_down(KeyCode.N):
            w.create_sprite(Pb2)

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
        


class Platform(Sprite):
    def on_create(self):
        self.scale = 100
        self.scale_x = 1080
        self.color = Color.AMBER
        self.add_tag('platform')
    def on_update(self, dt):
        pass


class Enemy(Sprite):
    def on_create(self):
        self.color = Color.MAGENTA
        self.health = w.create_sprite(EnemyHealth)
        self.scale = 20
        self.x = 300
        self.y = 114
        self.y_speed = 0
        self.is_touching_ground = False
        self.time = 0
        self.rotation = 180
    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag('pb'):
            for b in self.get_touching_sprites_with_tag('pb'):
                b.delete()
            self.health.width -= 5
            self.health.dx -= 2.5
        self.health.x = self.x + self.health.dx
        self.health.y = self.y + 20
        self.time += dt
        self.y += self.y_speed
        self.y_speed -= 0.5
        if self.health.width <= 0:
            self.delete()
        if not self.is_touching_ground:
            self.move_forward(5)
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
        self.move_forward(5)
        if self.is_touching_window_edge():
            self.delete()
        # if self.is_touching_sprite(player):
        #     if health.width > 5:
        #         health.width -= 5
        #         health.dx -= 2.5
        #     self.delete()





class EnemyHealth(Sprite):
    def on_create(self):
        self.color = Color.RED
        self.width = 50
        self.height = 2
        self.dx = 0
    def on_update(self, dt):
        pass


class Pb2(Sprite):
    def on_create(self):
        
        self.time = 0
        
        self.y_speed = 8
        self.x_speed = 8
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
p = w.create_sprite(Platform, x = 300, y = 100)
p.width = 100
p.height = 10
o = w.create_sprite(Platform, x = 500, y = 100)
o.width = 100
o.height = 10
w.create_sprite(Enemy)
w.create_sprite(Player)

w.run()
                                                                           