from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paying {amount} using Credit Card."

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paying {amount} using PayPal."

class PaymentSystem:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        return self.strategy.pay(amount)


payment = PaymentSystem(CreditCardPayment())
print(payment.execute_payment(100))

payment = PaymentSystem(PayPalPayment())
print(payment.execute_payment(200))
