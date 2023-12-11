class Vehicle:
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        return self.speed > other.speed

vehicle1 = Vehicle(name="BMW", speed=320, cost=70000)
vehicle2 = Vehicle(name="Mercedes", speed=280, cost=85000)
vehicle3 = Vehicle(name="Audi", speed=330, cost=62000)

vehicles = [vehicle1, vehicle2, vehicle3]

sorted_vehicles = sorted(vehicles, key=lambda x: x.speed, reverse=True)
for vehicle in sorted_vehicles:
    print(f"{vehicle.name} - Speed: {vehicle.speed} km/h, Cost; {vehicle.cost} $")