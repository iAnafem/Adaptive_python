class Cat:
    def __init__(self, age, name):
        self.hungry = True
        self.age = age
        self.name = name


    @property
    def descript(self):
        return f'{self.name} is {self.age}'

    def eat(self):
        if self.hungry:
            print('I am hangry...')
            self.hungry = False
        else:
            print('No, thanks!')

"""
class Barsik(Cat):
    def __init__(self):
        super(Barsik, self).__init__()
        self.sound = 'Aaaammm!'
        print(self.sound)

brs = Barsik()
brs.eat()
"""

c = Cat('Bars', 32)
print(c.descript)