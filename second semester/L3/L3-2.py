


from cProfile import label
from pycat.core import Window, Sprite, Color, Label
from random import randint

from tables import Col
w = Window()

ROW = 8
COL = 15
heatmap = []
CELL_SIZE = 50
X0 = 75
Y0 = w.height-75
class Cell(Sprite):
    def on_create(self):
        
        self.scale = CELL_SIZE - 1
        self.label = w.create_label()
        self.label.color = (0,0,0)

for i in range(ROW):
    rol = []
    for j in range(COL):
        rol.append(randint(0, 255))
    heatmap.append(rol)

for i in range(ROW):
    for j in range(COL):
        c = w.create_sprite(Cell)
        c.color = (255, 255-heatmap[i][j], 255-heatmap[i][j])
        c.x = X0 + j*CELL_SIZE
        c.y = Y0 - i*CELL_SIZE
        c.label.text = str(heatmap[i][j])
        c.label.x = c.x - c.label.content_width/2
        c.label.y = c.y + c.label.content_height/2





# print(heatmap)


w.run()