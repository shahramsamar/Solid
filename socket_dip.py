
from abc import ABC, abstractmethod

class Socket(ABC):
    @abstractmethod
    def provide_power(self):
        pass

class AmericanSocket(Socket):
    def provide_power(self):
        return "Providing 120V power with type A/B socket."

class EuropeanSocket(Socket):
    def provide_power(self):
        return "Providing 230V power with type C socket."

class UniversalAdapter:
    def __init__(self, socket: Socket):
        self.socket = socket

    def provide_power(self):
        return self.socket.provide_power()

class DeviceCharger:
    def charge(self, adapter: UniversalAdapter):
        power = adapter.provide_power()
        return f"Charging device using {power}"

european_socket = EuropeanSocket()
adapter = UniversalAdapter(european_socket)
charger = DeviceCharger()
print(charger.charge(adapter))

