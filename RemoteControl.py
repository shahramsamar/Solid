
class AllInOneRemote:
    def turn_on_tv(self):
        print("TV turned on!")

    def turn_off_tv(self):
        print("TV turned off!")

    def set_air_conditioner_temperature(self, temperature):
        print(f"Air conditioner temperature set to {temperature}°C")

    def play_sound_system(self):
        print("Sound system playing!")

    def stop_sound_system(self):
        print("Sound system stopped!")

    def turn_on_light(self):
        print("Light turned on!")

    def turn_off_light(self):
        print("Light turned off!")

    def set_oven_temperature(self, temperature):
        print(f"Oven temperature set to {temperature}°C")

remote = AllInOneRemote()
remote.turn_on_tv()
remote.set_air_conditioner_temperature(23)

