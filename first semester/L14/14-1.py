from pycat.base.event.mouse_event import MouseButton, MouseEvent
from pycat.core import Color, KeyCode, Sprite, Window,Scheduler
from random import randint

from pycat.label import Label

window = Window()

class Die(Label):
    def on_create(self):
        self.text = 'you lose'
        self.x = 540
        self.y = 340


class Player(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 30
        self.speed = 3
        self.has_weapon = False

    def die(self):
        window.delete_all_sprites()
        window.create_label(Die)
        Scheduler.cancel_update(spawn_enemy)
        


    def on_update(self, dt):
        # if self.is_touching_any_sprite_with_tag('eb'):
        #     health.width -= 5
            
        #     for b in self.get_touching_sprites_with_tag('eb'):
        #         b.delete()
        self.point_toward_mouse_cursor()
        if window.is_key_pressed(KeyCode.W):
            self.y += self.speed
        if window.is_key_pressed(KeyCode.A):
            self.x -= self.speed
        if window.is_key_pressed(KeyCode.S):
            self.y -= self.speed
        if window.is_key_pressed(KeyCode.D):
            self.x += self.speed
        # fill in code for keys A, S, D
    def on_left_click_anywhere(self):
        window.create_sprite(PlayerBullet)


class Enemy(Sprite):
    def on_create(self):
        self.color = Color.AZURE
        self.time = 0
        self.goto_random_position()
        self.scale = 30
        self.speed = 5
        self.rotation = randint(0, 360)
    def on_update(self, dt):
        self.move_forward(3)
        self.time += dt
        if self.time >= 1:
            b = window.create_sprite(EnemyBullet)
            b.position = self.position
            b.point_toward_sprite(player)
            self.time = 0
        if self.is_touching_window_edge() or self.is_touching_any_sprite_with_tag('pb'):
            self.delete()


class PlayerBullet(Sprite):
    def on_create(self):
        self.color = Color.CYAN
        self.scale = 10
        self.goto(player)
        self.point_toward_mouse_cursor()
        self.add_tag('pb')
    def on_update(self, dt):
        self.move_forward(5)
        if self.is_touching_window_edge():
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
            else:
                player.die()
            self.delete()


class PlayerBullet2(Sprite):
    def on_create(self):
        self.color = Color.TEAL
        self.scale = 10
        self.goto(player)
        self.add_tag('pb')
    def on_update(self, dt):
        self.move_forward(10)
        self.point_toward_sprite(Enemy)


class SpecialWeapon(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.scale = 3
    def on_update(self, dt):
        if self.is_touching_sprite(player):
            self.delete()
            player.has_weapon = True


player: Player = window.create_sprite(Player)
enemy = window.create_sprite(Enemy)
health: HealthBar = window.create_sprite(HealthBar)



def spawn_enemy(dt):
    window.create_sprite(Enemy)


Scheduler.update(spawn_enemy, delay=1)


def spawm_weapon(dt):
    window.create_sprite(SpecialWeapon)

Scheduler.update(spawm_weapon, delay=10)

window.run()