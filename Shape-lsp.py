
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def area(self):
        return self._width * self._height

class Square(Shape):
    def __init__(self, side):
        self._side = side

    def set_side(self, side):
        self._side = side

    def area(self):
        return self._side * self._side
