from pycat.core import Color, KeyCode, Sprite, Window
from random import randint
w = Window()


class Player(Sprite):
    def on_create(self):
        self.is_touching_ground = False
        self.y = 200
        self.scale = 15
        self.y_speed = 0
        self.layer = 2
    def on_update(self, dt):
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
                self.y += 1
        if w.is_key_down(KeyCode.B):
            w.create_sprite(PlayerBullet)


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
        self.scale = 20
        self.x = 300
        self.y = 114
        self.y_speed = 0
        self.is_touching_ground = False
        self.time = 0
        self.rotation = 180
    def on_update(self, dt):
        self.time += dt
        self.y += self.y_speed
        self.y_speed -= 0.5
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
        if self.is_touching_sprite(player):
            if health.width > 5:
                health.width -= 5
                health.dx -= 2.5
            self.delete()


class HealthBar(Sprite):
    def on_create(self):
        self.color = Color.RED
        self.width = 50
        self.height = 2
        self.y = player.y+30
        self.x = player.x
        self.dx = 0
    def on_update(self, dt):
        self.y = player.y+30
        self.x = player.x + self.dx


class EnemyHealth(Sprite):
    pass


w.create_sprite(Platform)
p = w.create_sprite(Platform, x = 300, y = 100)
p.width = 100
p.height = 10
o = w.create_sprite(Platform, x = 500, y = 100)
o.width = 100
o.height = 10
enemy = w.create_sprite(Enemy)
w.create_sprite(Player)
health: HealthBar = w.create_sprite(HealthBar)
w.run()
                                                                           
