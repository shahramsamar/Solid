
class TVRemote:
    def turn_on(self):
        print("TV turned on!")

    def turn_off(self):
        print("TV turned off!")

class AirConditionerRemote:
    def set_temperature(self, temperature):
        print(f"Air conditioner temperature set to {temperature}°C")

class SoundSystemRemote:
    def play(self):
        print("Sound system playing!")

    def stop(self):
        print("Sound system stopped!")

class LightRemote:
    def turn_on(self):
        print("Light turned on!")

    def turn_off(self):
        print("Light turned off!")

class OvenRemote:
    def set_temperature(self, temperature):
        print(f"Oven temperature set to {temperature}°C")

tv_remote = TVRemote()
tv_remote.turn_on()

ac_remote = AirConditionerRemote()
ac_remote.set_temperature(23)
