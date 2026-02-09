
class AmericanSocket:
    def provide_power(self):
        return "Providing 120V power with type A/B socket."

class EuropeanSocket:
    def provide_power(self):
        return "Providing 230V power with type C socket."

class AmericanPhoneCharger:
    def charge(self, socket: AmericanSocket):
        power = socket.provide_power()
        return f"Charging phone using {power}"

class EuropeanLaptopCharger:
    def charge(self, socket: EuropeanSocket):
        power = socket.provide_power()
        return f"Charging laptop using {power}"

american_socket = AmericanSocket()
charger = AmericanPhoneCharger()
print(charger.charge(american_socket))

