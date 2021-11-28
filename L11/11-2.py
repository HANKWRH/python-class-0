from pycat.core import Window, Sprite, Label
w = Window(background_image='L11_media/1.jpg')
label = w.create_label()
images = [
    'L11_media/1.jpg',
    'L11_media/2.jpg',
    'L11_media/3.jpg',
    'L11_media/4.jpg',
    'L11_media/5.jpg',
    'L11_media/6.jpg',
    'L11_media/7.jpg',
    'L11_media/8.jpg',
    'L11_media/9.jpg',
    'L11_media/10.jpg'
]
text_lable = [
    'bus',
    'bus stop1',
    'bus stop2',
    '',
    '',
    'bus stop3',
    '',
    '',
    '',
    ''
]

label.text = text_lable[0]


class NextButton(Sprite):
    def on_create(self):
        self.image = 'L11_media/nextbutton.png'
        self.x = 940
        self.y = 100
        self.scale = 0.5
        self.image_index = 0

    def on_left_click(self):
        self.image_index += 1
        if self.image_index >= len(images):
            self.image_index = 0
        
        w.background_image = images[self.image_index]
        label.text = text_lable[self.image_index]


w.create_sprite(NextButton)
w.run()