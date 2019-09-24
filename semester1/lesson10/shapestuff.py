from abc import ABC, abstractmethod
from math import pi

# Shapes
# get the perimeter/circumfrence 
# get the area
# print a summary of the shapes dimensions

class AbstractShape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def getPerimeter(self):
        pass
    
    @abstractmethod
    def getArea(self):
        pass
    
    @abstractmethod
    def dimensions(self):
        pass


class Rectangle(AbstractShape):

    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width

    def getPerimeter(self):
        permimeter = (self.length*2) + (self.width*2)
        return permimeter

    def getArea(self):
        area = self.length * self.width
        return area
    
    def dimensions(self):
        print(f"Rectangle with width {self.width} and length {self.length}")

    
class Circle(AbstractShape):

    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def getPerimeter(self):
        perimeter = 2*pi*self.radius
        return perimeter
    
    def getArea(self):
        area = pi*(self.radius**2) # or you can do math.pow(self.radius,2)
        return area

    def dimensions(self):
        print (f"Circle with radius{self.radius}")

    @property
    def diameter(self):
        return self.radius * 2


mycircle = Circle(10)
print(mycircle.getArea())
print(mycircle.getPerimeter())
print(mycircle.diameter)