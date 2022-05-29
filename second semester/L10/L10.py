from pycat.core import Window, Sprite, Scheduler, Color, Label
from random import randint, choice
from enum import Enum, auto
w = Window(enforce_window_limits=False)

class Group(Enum):
    SPORTS = auto()
    ANIMALS = auto()
words = dict()
words[Group.ANIMALS] = ['cat', 'bear', 'dinosaur']
words[Group.SPORTS]  = ['baseball',  'volleyball', 'badminton']
# <(x_x)>
<<<<<<< HEAD
# o-[x_x]-o
# [x_x] (x_x)
=======

>>>>>>> b4c2816741fd60ebd56004b795f91031696d453c
class Label(Label):
    def on_create(self):
        self.scale = 100
        self.x = w.width
        self.y = w.height
        self.label_group = w.create_label()
        self.label_group.text = str(Words.current_group)
    def on_update(self, dt: float):
        self.label_group.text = str(Words.current_group)


class Score(Label):
    def on_create(self):
        self.x = 1080
        self.score = 0
    def on_update(self, dt: float):
        self.text = 'score:'+str(self.score)

    
class Words(Sprite):
    current_group = choice(list(words))
    def on_create(self):
        
        self.scale = 100
        self.color = Color.BLUE
        self.x = randint(0, w.width)
        self.y = w.height
        self.label = w.create_label()
        self.label.text = choice(words[choice(list(words))])
        self.width = self.label.content_width*1.2
        self.height = self.label.content_height*1.2
        self.label.x = self.x - 0.5*self.width + 0.1*self.width
        self.label.y = self.y + 0.5*self.height - 0.1*self.height
    def on_update(self, dt):
        self.y -= 2
        self.label.y = self.y + 0.5*self.height - 0.15*self.height
        if self.y <= 0:
            self.delete()
    def delete(self):
        super().delete()
        self.label.delete()
    def on_left_click(self):
        if self.label.text in words[Words.current_group]:
            score.score += 1
        self.delete()

def switch_group():
    Words.current_group = choice(list(words))
    Scheduler.wait(randint(2,5), switch_group)
    print(Words.current_group)
switch_group()

def spwan_label(dt):
    w.create_sprite(Words)
Scheduler.update(spwan_label,delay= 1)
w.create_label(Label)
score = w.create_label(Score)
w.run()