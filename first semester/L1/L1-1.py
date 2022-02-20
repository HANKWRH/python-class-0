from pycat.core import Window
from pyglet.image import create
answer = input('which animal do you want to see:')
size = input('do you want your animal B or S?')
window = Window()


animal = window.create_sprite()
if answer == 'pig':
    animal.image = 'pig.png'
elif answer == 'owl':
    animal.image = 'owl.gif'
else:
    print('sorry')
if size == 'B':
    animal.scale = 3
elif size == 'S':
    animal.scale =0.5
else:
    pass

animal.x = 500
animal.y = 500
window.run()

