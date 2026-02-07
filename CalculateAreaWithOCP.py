
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    @staticmethod
    def calculate_area(shape):
        return shape.area()

rectangle = Rectangle(5, 10)
circle = Circle(5)
calculator = AreaCalculator()

print(calculator.calculate_area(rectangle))  # Output: 50
print(calculator.calculate_area(circle))     # Output: 78.5