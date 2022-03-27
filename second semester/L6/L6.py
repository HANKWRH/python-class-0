from pycat.core import Sprite, Window, Color
from typing import List
from random import randint

from tables import Col

w = Window()

ROWS = 6
COLS = 10
X0 = 70
Y0 = w.height - 70
CELL_SIZE = 100

grid:List[List['Cell']] = []

class Cell(Sprite):
    def on_create(self):
        self.scale = CELL_SIZE-1
        self.x=X0
        self.y=Y0
        self.i = -1
        self.j = -1
        

    def set_up(self,i,j):
        self.x = X0+j*CELL_SIZE
        self.y = Y0-i*CELL_SIZE
        self.i = i
        self.j = j

    def on_left_click(self):
        print(self.i,self.j)
        self.toggle_neighbors()
        check()
    
    def toggle_neighbors(self):
        if self.i > 0:
            grid[self.i-1][self.j].toggle()
        if self.i < ROWS-1:
            grid[self.i+1][self.j].toggle()
        if self.j > 0:
            grid[self.i][self.j-1].toggle()
        if self.j < COLS-1:
            grid[self.i][self.j+1].toggle()
    def toggle(self):
        if self.color == Color.RED:
            self.color = Color.WHITE
        else:
            self.color = Color.RED




for i in range(ROWS):
    row=[]
    for j in range(COLS):
        c = w.create_sprite(Cell)
        c.set_up(i,j)
        row.append(c)
    grid.append(row)

def check():
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j].color == Color.RED:
                return
    
    w.close()


for a in range(10):
    i = randint(0,ROWS-1)
    j = randint(0,COLS-1)
    grid[i][j].toggle_neighbors()



w.run()