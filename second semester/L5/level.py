from tkinter import W
from pycat.core import Window, Sprite, Color, Label, KeyCode
from level_builder import level_builder


w = Window(is_sharp_pixel_scaling=True)

LEVEL = [
    'ggggggg',
    'gwwwwwg',
    'gwwwwwgggggg',
    'gwwwwwwwwwSg',
    'gwwwwwwwwwwg',
    'gggggggggggg',
]

LEVEL2 = [
    '',
    '',
    'gggggggggggg',
    'gwwwwwwwwwsg',
    'gwwwwwwwwwwg',
    'gggggggggggg',
]

LEVEL_D = {
    'w':('tiles/tile_019.png', 'ground'),
    'g':('tiles/tile_012.png', 'wall'),
    's':('tiles/tile_013.png', 'stair'),
    'S':('tiles/tile_014.png', 'stair')
}
CELL_SIZE = 50
X0 = 70
Y0 = w.height-70

class Player(Sprite):
    def on_create(self):
        self.x = X0+CELL_SIZE
        self.y = Y0-CELL_SIZE
        self.layer=2
        
        self.image = 'tiles/tile_199.png'
        self.scale_to_width(CELL_SIZE-1)
    def on_update(self, dt):
        if w.is_key_down(KeyCode.W):
            self.y += CELL_SIZE
            if self.is_touching_any_sprite_with_tag('g'):
                self.y -= CELL_SIZE
        if w.is_key_down(KeyCode.S):
            self.y -= CELL_SIZE
            if self.is_touching_any_sprite_with_tag('g'):
                self.y += CELL_SIZE
        if w.is_key_down(KeyCode.D):
            self.x += CELL_SIZE
            if self.is_touching_any_sprite_with_tag('g'):
                self.x -= CELL_SIZE
        if w.is_key_down(KeyCode.A):
            self.x -= CELL_SIZE
            if self.is_touching_any_sprite_with_tag('g'):
                self.x += CELL_SIZE
level_builder(LEVEL, LEVEL_D, w, CELL_SIZE, X0, Y0,'L1')
level_builder(LEVEL2, LEVEL_D, w, CELL_SIZE, 700, Y0,'L2')
w.create_sprite(Player)


w.run()