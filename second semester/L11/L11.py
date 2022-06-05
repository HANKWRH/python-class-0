from pycat.core import Window, Sprite, Scheduler, Color, Label
from random import randint, choice
from enum import Enum, auto
from os.path import dirname

w = Window(enforce_window_limits=False)
with open(dirname(__file__)+'/score.txt','r') as file:
    highscore = int(file.readline())
class Group(Enum):
    SPORTS = auto()
    ANIMALS = auto()
words = dict()
# words[Group.ANIMALS] = ['cat', 'bear', 'dinosaur']
# words[Group.SPORTS]  = ['baseball',  'volleyball', 'badminton']
# <(x_x)>
with open(dirname(__file__)+'/sports.txt','r') as file:
    words[Group.SPORTS] = [w.strip() for w in file.readlines()]
with open(dirname(__file__)+'/animals.txt','r') as file:
    words[Group.ANIMALS] = [w.strip() for w in file.readlines()]


class Highscore(Label):
    def on_create(self):
        self.x = 540
        self.score = 0
    def on_update(self, dt: float):
        self.text = 'Highscore:' + str(highscore)
        if score.score > highscore:
            self.text = 'Highscore:' + str(score.score)

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
        self.text = 'Score:'+str(self.score)

        

    
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
            with open(dirname(__file__)+'/score.txt','r') as file:
                highscore = int(file.readline())
            if highscore < score.score:
                with open(dirname(__file__)+'/score.txt','w') as file:    
                    file.write(str(score.score))
        self.delete()

def switch_group():
    Words.current_group = choice(list(words))
    Scheduler.wait(randint(2,5), switch_group)
switch_group()

def spwan_label(dt):
    w.create_sprite(Words)
Scheduler.update(spwan_label,delay= 1)
w.create_label(Label)
score = w.create_label(Score)
w.create_label(Highscore)
w.run()