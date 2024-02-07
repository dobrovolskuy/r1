from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def display_info(self):
        pass

class Sedan(Car):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display_info(self):
        print(f"Brand = {self.brand}")
        print(f"Model = {self.model}")
        print(f"Type = Sedan")
        print(f"Doors = {self.doors}")

class SUV(Car):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_info(self):
        print(f"Brand = {self.brand}")
        print(f"Model = {self.model}")
        print(f"Type = SUV")
        print(f"Seats = {self.seats}")

class SportsCar(Car):
    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Type: Sports Car")
        print(f"Max speed: {self.max_speed} km/h")

sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Jeep", "Grand Cherokee", 5)
sports_car = SportsCar("Ferrari", "LaFerrari", 350)

sedan.display_info()
print("-----------------------")
suv.display_info()
print("-----------------------")
sports_car.display_info()


