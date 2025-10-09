import streamlit as st

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def start(self):
        return f"{self.brand} {self.model} is starting."
class Car(Vehicle):
    def play_music(self):
        return f"{self.brand} {self.model} is playing music."
class ElectricVehicle(Vehicle):
    def charge(self):
        return f"{self.brand} {self.model} is charging."
class SmartDevice:
    def connect_wifi(self, brand, model):
        return f"{brand} {model} connected to WiFi."
class SmartCar(Car, SmartDevice):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def autodrive(self):
        return f"{self.brand} {self.model} is in automatic mode."
class Bike(Vehicle):
    def kick_start(self):
        return f"{self.brand} {self.model} is a bike and started with a kick."
class ElectricSmartCar(SmartCar, ElectricVehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def autopilot_mode(self):
        return f"{self.brand} {self.model} is in Autopilot mode."
    
st.title("VEHICLE REVIEWER")
st.header("Electric Smart Car Details")
brand_ec = st.text_input("Enter the brand of Electric Smart Car:")
model_ec = st.text_input("Enter the model of Electric Smart Car:")

if st.button("Show Electric Smart Car Features"):
    if brand_ec and model_ec:
        ec = ElectricSmartCar(brand_ec, model_ec)
        st.success(ec.autopilot_mode())
        st.info(ec.autodrive())
        st.warning(ec.charge())
        st.write(ec.play_music())
        st.write(ec.connect_wifi(ec.brand, ec.model))
        st.write(ec.start())
    else:
        st.error("Please enter both brand and model.")

st.header("Bike Details")
brand_bike = st.text_input("Enter the brand of Bike:")
model_bike = st.text_input("Enter the model of Bike:")

if st.button("Show Bike Features"):
    if brand_bike and model_bike:
        bi = Bike(brand_bike, model_bike)
        st.success(bi.kick_start())
        st.write(bi.start())
    else:
        st.error("Please enter both brand and model.")