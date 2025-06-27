# Dice in Games
from random import randint

class Dice:
    def __init__(self,sides):
        self.sides = sides

    def roll_dice(self):
        return randint(1,self.sides)
    
d1 = Dice(6)
print(d1.roll_dice())
print(d1.roll_dice())




# Class for circle
import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius *self.radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
a = Circle(4)
print(a.area())
print(a.perimeter())