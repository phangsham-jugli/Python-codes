#Abstract class
import math
from my_abstract_class import shape

class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

class Square(shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side **2

class Circle(shape):
    def __init__(self,radius):
        self.r=radius

    def area(self):
        return math.pi*(self.r**2)


R=Rectangle(2,3)
print(R.area())
print("\n")

S=Square(4)
print(S.area())
print("\n")

C=Circle(2)
print(C.area())

#----Without area method in every class it would be an error we can do like EG1 in notes of abstract class
