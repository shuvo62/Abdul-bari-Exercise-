from random import *
class dice:
    def __init__(self, sides):
        self.sides = sides
    def roll_dice(self):
        return randint(1, self.sides)
d1 = dice(8)
print(d1.roll_dice())
print(d1.roll_dice())