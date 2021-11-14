from pycat.core import Window, Sprite, AudioLoop, Player
from pyglet import window
from random import shuffle
from typing import List

w = Window(draw_sprite_rects=True, background_image='L8.image/forest_04.png')
click = Player('L8.image/hit.wav')
no_match_music = Player('L8.image/laugh.wav')
match_music = Player('L8.image/point.wav')
audio_loop = AudioLoop('L8.image/LoopLivi.wav')
audio_loop.play()

clicked_list :List['Card'] = []
img_list = 4*['L8.image/1.png', 'L8.image/2.png', 'L8.image/3.png', 'L8.image/4.png']
shuffle(img_list)
class Button(Sprite):
    def on_create(self):
        self.image ='L8.image/button.png'
        self.x = 800
        self.y = 300
        self.scale = 0.5
    def on_left_click(self):
        if len(clicked_list) ==2:
            if clicked_list[0].image == clicked_list[1].image:
                clicked_list[0].state = 1
                clicked_list[1].state = 1
                # clicked_list[0].delete()
                # clicked_list[1].delete()
                #Card.total -= 2
                match_music.play()
                # if Card.total == 0:
                #     print(Card.total, 'you win')
            else:
                clicked_list[0].is_visible =False
                clicked_list[1].is_visible =False
                no_match_music.play()
            clicked_list.clear()
               
                

class Card(Sprite):
    total = 0  # static variable
    def on_create(self):
        self.state = 0
        self.image = img_list.pop()
        self.is_visible = False
        self.scale = 1.5
        Card.total += 1
    def on_left_click(self):
        if self not in clicked_list and len(clicked_list) < 2:
            clicked_list.append(self)
            click.play()
            self.is_visible = True
    def on_update(self, dt):
        if self.state == 1:
            self.rotation += 1
            self.scale -= 0.01
            if self.rotation >= 180:
                self.delete()
                Card.total -= 1
                if Card.total == 0:
                    
                    w.draw_sprite_rects = False
                    w.delete_all_sprites()
                    w.create_sprite(Win)
class Win(Sprite):
    def on_create(self):
        self.state1 = 0
        self.state2 = 0
        self.image = 'L8.image/win.png'
        self.x = 640
        self.y = 340
    def on_update(self, dt):
        self.rotation += 1
        self.scale += 0.01
        if self.rotation == 360:
            self.state1 = 1
        if self.state1 == 1:
            self.rotation = 360
        if self.scale >= 2:
            self.state2 = 1
        if self.state2 == 1:
            self.scale = 2
        
for i in range(4):
    for j in range(4):
        w.create_sprite(Card, x = 100+j*110, y = 200+i*110)

    # label = w.create_label()
    # label.text = ''
w.create_sprite(Button)       
    

w.run()
