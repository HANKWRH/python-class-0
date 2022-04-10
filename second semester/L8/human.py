from os import name


class Human:

    def __init__(self, age, name):
        self.name = name
        self.age = age
    
    def talk(self):
        print('I am', self.name, 'I am', self.age)

h = Human(10, 'Hank')
h.talk()