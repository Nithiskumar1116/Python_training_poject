class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def start(self):
        print(f"{self.brand} {self.model} is starting.")
class Car(Vehicle):
    def play_music(self):
        print(f"{self.brand} {self.model} is playing music.")
class ElectricVehicle(Vehicle):
    def charge(self):
        print(f"{self.brand} {self.model} is charging.")
class SmartDevice:
    def __init__(self):
        pass
    def connect_wifi(self, brand, model):
        print(f"{brand} {model} connected to WiFi.")
class SmartCar(Car, SmartDevice):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def autodrive(self):
        print(f"{self.brand} {self.model} is in automatic mode.")
class Bike(Vehicle):
    def kick_start(self):
        print(f"{self.brand} {self.model} is bike and started with a kick.")
class ElectricSmartCar(SmartCar, ElectricVehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def autopilot_mode(self):
        print(f"{self.brand} {self.model} is in Autopilot mode.")
brand_ec = input("Enter the brand of electric smart car: ")
model_ec = input("Enter the model of electric smart car: ")
ec = ElectricSmartCar(brand_ec,model_ec)
ec.autopilot_mode()
ec.autodrive()
ec.charge()
ec.play_music()
ec.connect_wifi(ec.brand, ec.model)
ec.start()
brand_bike = input("Enter the brand of bike: ")
model_bike = input("Enter the model of bike: ")
bi = Bike(brand_bike,model_bike)
bi.kick_start()
bi.start()