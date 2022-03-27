from pycat.core import Window, Sprite
from typing import List, Dict, Tuple


def level_builder(level: List[str], level_img: Dict[str, Tuple[str, str]], window: Window, cell_size: float, x0: int, y0: int, tag:str):


    class Cell(Sprite):
        def on_left_click(self):
            print(self.image)
            self.add_tag(tag)
    for i in range(len(level)):
        for j in range(len(level[i])):
            a = level[i][j]
            c = window.create_sprite(Cell)
            c.image = level_img[a][0]
            c.add_tag(a)
            c.x = x0 + j*cell_size
            c.y = y0 - i*cell_size
            c.scale_to_width(cell_size)
            

    print('test')