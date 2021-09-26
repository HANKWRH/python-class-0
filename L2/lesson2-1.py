from random import Random
from pycat.core import Window, Color
from pycat.sprite import Sprite
w = Window()

#x = input('enter your X:')
#y = input('enter your Y:')
#size = input('big or small:')

class Owl(Sprite):

    def on_create(self):
        self.image = "owl.gif"
        self.goto_random_position()
        self.scale = 1
        self.color = Color(255,0,0)
class Fireball(Sprite):

    def on_create(self):
        self.image = "fireball.gif"
        self.opacity = 100
        self.goto_random_position()
        
        self.scale = 1.5
for i in range(10):#loop
    w.create_sprite(Fireball)
    w.create_sprite(Owl)



#animal = w.create_sprite()
#animal.image = 'fireball.gif'
#animal.x = float(x)
#animal.y = float(y)

#p = ('my sprite has image = ' + animal.image
#                              + ',x = ' + str(animal.x)
#                              + ',y = ' + str(animal.y))
#print(p)


w.run()