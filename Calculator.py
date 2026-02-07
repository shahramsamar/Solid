# strategy pattern
# without   Open Close Principle

class SimpleCalculator:
    def operation(self, op_type, a, b):
        if op_type == "add":
            return a + b
        elif op_type == "subtract":
            return a - b

calc = SimpleCalculator()
print(calc.operation("add", 5, 3))  # Outputs: 8


# Open Close Principle

from abc import ABC, abstractmethod

class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Add(OperationStrategy):
    def execute(self, a, b):
        return a + b

class Subtract(OperationStrategy):
    def execute(self, a, b):
        return a - b

class SimpleCalculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def operation(self, a, b):
        return self.strategy.execute(a, b)

class Multiply(OperationStrategy):
    def execute(self, a, b):
        return a * b

multiply_strategy = Multiply()
calc = SimpleCalculator(multiply_strategy)
print(calc.operation(5, 3))  # Outputs: 15

