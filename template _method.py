
class Vehicle:
    def operateVehicle(self):
        self.startEngine()
        self.move()
        self.stopEngine()

    def startEngine(self):
        print("Starting engine")

    def move(self):
        print("Moving")

    def stopEngine(self):
        print("Stopping engine")

class Car(Vehicle):
    def startEngine(self):
        print("Starting car engine")

    def stopEngine(self):
        print("Stopping car engine")

class Bicycle(Vehicle):
    def startEngine(self):
        # Overriding to do nothing for a bicycle
        pass

    def stopEngine(self):
        # Overriding to do nothing for a bicycle
        pass

my_car = Car()
my_bicycle = Bicycle()

print("Operating a car:")
my_car.operateVehicle()

print("\nOperating a bicycle:")
my_bicycle.operateVehicle()
