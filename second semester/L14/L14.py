from pycat.core import Window, Sprite
from enum import Enum, auto

w = Window()

class ApeState(Enum):
    WAIT = auto()
    LEFT_UP = auto()
    RIGHT_UP = auto()

    
class Barrel(Sprite):

    def on_create(self):
        self.image = 'img/barrel1.png'
        self.position = ape.position
    def on_update(self, dt):
        self.y -= 5
        if self.is_touching_window_edge():
            self.delete()
        # for i in range(1,5):
        #     self.image = 'img/barrel'+str(i)+'.png'


class Ape(Sprite):

    def on_create(self):
        self.time = 0
        self.x = 100
        self.y = 200
        self.image = 'img/ape_waiting.png'
        self.state = ApeState.WAIT
        self.left_right_times = 0

    def on_update(self, dt):
        self.time += dt
        if self.state is ApeState.WAIT:
            if self.time >= 2:
                self.state = ApeState.LEFT_UP
                self.image = 'img/ape_angry1.png'
                self.time = 0
        
        if self.state is ApeState.LEFT_UP:
            if self.time >= 1:
                self.state = ApeState.RIGHT_UP
                self.image = 'img/ape_angry2.png'
                self.time = 0
        
        if self.state is ApeState.RIGHT_UP:
            if self.time >= 1:
                self.left_right_times += 1
                if self.left_right_times > 4:
                    w.create_sprite(Barrel)
                    self.state = ApeState.WAIT
                    self.image = 'img/ape_waiting.png'
                    self.left_right_times = 0
                else:
                    self.image = 'img/ape_angry1.png'
                    self.time = 0
                    self.state = ApeState.LEFT_UP
        
ape = w.create_sprite(Ape)
w.run()