from pycat.core import Window, Sprite
from pyglet import window
from random import shuffle
w = Window(draw_sprite_rects=True)
clicked_list = []
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
                clicked_list[0].delete()
                clicked_list[1].delete()
            else:
                clicked_list[0].is_visible =False
                clicked_list[1].is_visible =False
            clicked_list.clear()
               
                

class Card(Sprite):
    def on_create(self):
        self.image = img_list.pop()
        self.is_visible = False
        self.scale = 1.5
    def on_left_click(self):
        if len(clicked_list) < 2:
            clicked_list.append(self)
            self.is_visible = True
            
for i in range(4):
    for j in range(4):
        w.create_sprite(Card, x = 100+j*110, y = 200+i*110)

    # label = w.create_label()
    # label.text = ''
w.create_sprite(Button)       
    

w.run()