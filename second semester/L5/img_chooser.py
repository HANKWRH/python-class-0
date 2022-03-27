from cProfile import label
from pycat.core import Window, Sprite, Color, Label
from random import randint

from tables import Col
w = Window(is_sharp_pixel_scaling=True)

ROW = 12
COL = 24
heatmap = []
CELL_SIZE = 50
X0 = 20
Y0 = w.height-20
class Cell(Sprite):
    def on_left_click(self):
        print(self.image)
value = 0
for i in range(ROW):
    rol = []
    for j in range(COL):
        rol.append(value)
        value = value+1  
    heatmap.append(rol)


for i in range(ROW):
    for j in range(COL):
        c = w.create_sprite(Cell)
        c.x = X0 + j*CELL_SIZE
        c.y = Y0 - i*CELL_SIZE
        value=heatmap[i][j]
        numstr=""
        if value < 10:
            numstr = '00'+str(value)
        elif 10<=value<100:
            numstr = '0'+str(value)
        else:
            numstr = str(value)
        c.image = 'tiles/tile_'+numstr+'.png'
        c.scale_to_width(CELL_SIZE)





# print(heatmap)


w.run()