from pycat.core import Window,  KeyCode, Sprite, RotationMode, Color, Scheduler
from random import randint

w = Window(background_image='L6_media/underwater.png')
label = w.create_label()
label.text = 'Score = '
class Ship(Sprite):
    def on_create(self):
        self.score = 0
        self.type = 1
        self.image = 'L6_media/spaceship.png'
        self.x = 10
        self.y = 600
        self.scale = 0.3
        self.scale_y = 0.7
        
    def on_update(self, dt):
        label.text = 'Score = '+str(self.score)
        if self.type ==0:
            self.x -=5
        if self.type == 1:
            self.x += 5
        if self.x >= 1280:
            self.type = 0
        if self.x <= 0:
            self.type = 1
class Alien(Sprite):
    def on_create(self):
        img_num = randint(1,5)
        self.image = 'L6_media/'+str(img_num)+'.png'
        self.goto_random_position()
        self.y = 50
        self.scale = 0.3
        self.is_click = False
        self.add_tag('alien')
        self.moving_type = 0
    def on_update(self, dt):
        # if self.y >= 70:
        #     self.moving_type = 1
        # if self.y <= 0:
        #     self.moving_type = 0
        # if self.moving_type == 0:
        #     self.x += 2
        #     self.y += 2
        # if self.moving_type == 1:
        #     self.x += 2
        #     self.y -= 2
        if self.is_click == True:
            self.y += 10
        if self.y >= 640:
            self.delete()
        if self.is_touching_sprite(ship):
            self.delete()
            ship.score += 1
            # print(ship.score)
        

    def on_left_click(self):
        self.is_click = True
def create_alien():
    w.create_sprite(Alien)
Scheduler.update(create_alien,1)
ship = w.create_sprite(Ship)
w.run()