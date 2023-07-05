from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating instances of the concrete classes
rectangle = Rectangle(4, 5)
circle = Circle(3)

# Accessing area and perimeter using the abstraction
print("Rectangle:")
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

print("\nCircle:")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
