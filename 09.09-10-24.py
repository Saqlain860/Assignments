#abstraction

from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def figur(self):
        return "it is 2 dimentinoal plane figure"
    
class Rectangle(Polygon):
    def sides(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

    def extramethod(self):
        return "Rectangle having 2 sides"

class Square(Polygon):
    def sides(self,side):
        self.side = side
    
    def area(self):
        return self.side*self.side

    def perimeter(self):
        return 4*self.side

    def extramethod(self):
        return "Square having 4 sides"
rect = Rectangle()
rect.sides(10,20)
squa = Square()
squa.sides(10)

for obj in [rect,squa]:
    print(obj.area())
    print(obj.perimeter())
    print(obj.extramethod())
    print(obj.figur())