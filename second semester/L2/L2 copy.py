from pycat.core import Window, Sprite
from enum import Enum
w = Window(background_image='mountains.png')
GRAVITY = -0.2
SPEED_SCALE = 0.03
class AliienState(Enum):
    WAIT = 0
    JUMP = 1
class Player(Sprite):
    def on_create(self):
        self.state = AliienState.JUMP
        self.x_speed = 0
        self.y_speed = 0
        self.image = 'alien.png'
        self.scale = 0.2
        self.layer = 1
    def on_update(self, dt):
        
        
        if self.state is AliienState.JUMP:
            self.y_speed += GRAVITY
            self.x += self.x_speed
            prev_y = self.y - self.y_speed
            self.y += self.y_speed
            if self.is_touching_window_edge():
                self.x = a.x
                self.y = a.y + self.height/2 + a.height/2
                self.state = AliienState.WAIT
            else:
                list_t = self.get_touching_sprites_with_tag('hit')
                if list_t:
                    p = list_t[0]
                    min_y = p.y + self.height/2 + p.height/2
                    if prev_y > min_y:
                        self.state = AliienState.WAIT
                        self.y = min_y
                    else:
                        pass
    def on_left_click_anywhere(self):
        if self.state is AliienState.WAIT:
            dx = w.mouse_position.x - self.x
            dy = w.mouse_position.y - self.y
            self.x_speed = dx*SPEED_SCALE
            self.y_speed = dy*SPEED_SCALE
            self.state = AliienState.JUMP

class Platform(Sprite):
    def on_create(self):
        self.add_tag('plat')
        self.scale = 0.3
        self.image = 'platform.png'
        self.hitbox = w.create_sprite(Hitbox)
        self.hitbox.width = self.width * 0.8
        self.hitbox.height = self.height*0.1
    
    def set_hitbox(self):
        self.hitbox.x = self.x
        self.hitbox.y = self.y+5

class Platform2(Sprite):
    def on_create(self):
        self.add_tag('plat')
        self.scale = 0.3
        self.image = 'platform.png'
        self.hitbox = w.create_sprite(Hitbox)
        self.hitbox.width = self.width * 0.8
        self.hitbox.height = self.height*0.1
    
    def on_update(self, dt):
        self.opacity -=1
    
    def set_hitbox(self):
        self.hitbox.x = self.x
        self.hitbox.y = self.y+5
    
class Hitbox(Sprite):
    def on_create(self):
        self.opacity=0
        self.add_tag('hit')
        self.layer=1

        
        

a = w.create_sprite(Platform, x=100, y=300)
player = w.create_sprite(Player)

b = w.create_sprite(Platform, x=300, y=200)
c = w.create_sprite(Platform, x=800, y=400)
d = w.create_sprite(Platform, x=600, y=200)
e = w.create_sprite(Platform2, x=700, y=100)
f = w.create_sprite(Platform, x=1200, y=250)
for p in w.get_sprites_with_tag('plat'):
    p.set_hitbox()

player.x = a.x
player.y = a.y + player.height/2 + a.height/2
w.run()