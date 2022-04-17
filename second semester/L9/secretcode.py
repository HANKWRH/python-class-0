from turtle import color
from pycat.core import Window, Color, Sprite
from random import choice
from typing import List



class People(Sprite):
    def on_create(self):
        pass

w = Window(draw_sprite_rects=True)
w.set_clear_color(77, 77, 77)
SCALE = 50
PEGS = 4
GUESS = 10
COLORS = [Color.RED
        , Color.BLACK
        , Color(204, 255, 153)
        , Color(0, 102, 0)
        , Color(255, 102, 204)
        , Color(0, 0, 225)
        , Color(102, 51, 0)
        , Color.PURPLE]
code = []
guess_color = COLORS[0]
for i in range(PEGS):
    s = w.create_sprite()
    s.color = choice(COLORS)
    print(s.color)
    code.append(s.color)
    s.scale = SCALE
    s.y = w.height-s.height/2
    s.x = s.width/2 + i*s.width

class Guess:
    def __init__(self, y):
        self.sprites: List[ColorGuess] = []
        self.y = y
        for i in range(PEGS):
            b = w.create_sprite(ColorGuess)
            b.scale = SCALE
            b.y = y
            b.x = b.width/2 + i*b.width
            self.sprites.append(b)
class ColorGuess(Sprite):
    def on_left_click(self):
        if self in g.sprites:      
            self.color = guess_color

class ColorChoice(Sprite):
    def on_left_click(self):
        global guess_color
        guess_color = self.color
class ColorChooser:
    def __init__(self):
        for i in range(len(COLORS)):
            a = w.create_sprite(ColorChoice)
            a.color = COLORS[i]
            a.scale = 30
            a.y = a.height/2
            a.x = a.width/2 + i*a.width


class CheckBottom(Sprite):
    def on_create(self):
        self.scale_x = 20
        self.scale_y = 10
        self.x = 500
        self.y = 300

    def on_left_click(self):
        global g
        red=0
 
        for i in range(PEGS):
            color = g.sprites[i].color
            if code[i] == color:
                red+=1
        print('red:',red)
        g=Guess(g.y+SCALE)

w.create_sprite(CheckBottom)
ColorChooser()
g=Guess(2*SCALE)
w.run()