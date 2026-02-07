
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class AreaCalculator:
    def calculate_area(self, shape):
        return shape.width * shape.height

rectangle = Rectangle(5, 10)
calculator = AreaCalculator()
print(calculator.calculate_area(rectangle))  # Output: 50

