#??????????????
''' import math

class Shape():
    def area(self):
        pass
           


class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
        pass
class Rectangle(Shape):
    def __init__(self,width,length):
        self.width=width
        self.length=length
        pass
class Triangle(Shape):
    def __init__(self,length,height):
        self.length=length
        self.height=height
        pass

my_shapes=[Circle(5),Rectangle(5,10),Triangle(10,15)]
for area in my_shapes:
    print(area())'''

'''from abc import ABC, abstractmethod

class Drawable (ABC):
    @abstractmethod
    def draw(self):
        pass
class Circle(Drawable):
    def draw(self):
        print("Draw the circle")

class Rectangle(Drawable):
    def draw(self):
        print("Draw the rectangle")

class Triangle(Drawable):
    def draw(self):
        print("Draw the triangle")
shapes=[Circle(),Rectangle(),Triangle()]
for shape in shapes:
    shape.draw()'''

import math

class Numbers():
    def __init__ (self,a,b):
        self.a=a
        self.b=b

    def __mul__(self):
        return self.a*self.b
    def __neg__(self):
        return self.a-self.b
    def __sub__(self):
        return self.a+self.b
object1=Numbers(35.100)
object2=Numbers(5.10)
object3=Numbers(15.30)

object1.mul()
object2.neg()
object3.sub()