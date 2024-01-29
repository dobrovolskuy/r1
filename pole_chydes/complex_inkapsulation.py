
class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def get_make(self):
        return self.__make

    def set_make(self, new_make):
        self.__make = new_make

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model

    def drive(self, distance):
        if self.mileage + distance > 300000:
            print("Mileage limit reached. Unable to make the trip")
        else:
            self.mileage += distance
            print(f"The trip took place. New run: {self.mileage} km.")

car = Car("Audi", "A4", 2021, 27000)

print(car.get_make())
print(car.get_model())

car.set_make("Honda")
car.set_model("Accord")

print(car.get_make())
print(car.get_model())