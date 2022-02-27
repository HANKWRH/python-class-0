from cProfile import label
from venv import create
from pycat.core import Window, Sprite, Scheduler, KeyCode, Label, Color
from random import randint
w = Window(enforce_window_limits=False, width=1800, height=1008, background_image='background.png')
w.background_sprite.scale=2

class Lose(Label):
    def on_create(self):
        self.x = 540
        self.y = 540
        self.color = Color.RED
        self.font_size = 200
        self.text = 'Lose'
       
    def on_update(self, dt: float):
        pass

class Score(Label):
    def on_create(self):
        self.x = 50
        self.y = 1000
        self.score = 0
    def on_update(self, dt: float):
        self.text = 'Score = '+str(self.score)
        if self.score == 20:
            w.background_image = 'moon.jpg'
            w.background_sprite.scale = 1008/360


label = w.create_label(Score)



class Bird(Sprite):
    def on_create(self):
        self.y_speed = 0
        self.image = 'bird.gif'
        self.scale = 0.5
        self.y = w.width/2
        self.x = 65
        score = 0
    def on_update(self, dt):
        if w.is_key_down(KeyCode.SPACE):
            if w.background_image == 'moon.png':
                pass
            else:
                self.y_speed = 5
                self.rotation += 15
            self.rotation -= 0.31
            self.y_speed -= 0.2
            self.y += self.y_speed
            if self.is_touching_any_sprite_with_tag('pipe') or self.is_touching_window_edge():
                w.delete_all_sprites()
                Scheduler.cancel_update(create_pipe)
                w.create_label(Lose)

bird = w.create_sprite(Bird)

min_pipe_y = -120
pipe_gap = 300

class Pipe(Sprite):
    def on_create(self):
        self.image = 'pipe.png'
        self.scale = 1
        self.y = 0
        self.x = w.width + self.width/2
        self.scale_y = 1.5
    def on_update(self, dt):
        self.x -= 5
        if self.x <= - self.width/2:
            self.delete()
            label.score += 0.5

def create_pipe(dt):
    dy = randint(0, 200)
    pB = w.create_sprite(Pipe)
    pB.y = min_pipe_y + dy
    pB.add_tag('pipe')
    pT = w.create_sprite(Pipe)
    pT.y = min_pipe_y + pipe_gap + pB.height + dy
    pT.rotation = 180
    pT.add_tag('pipe')
    
Scheduler.update(create_pipe, 1.5)

create_pipe(0)
w.run()