class Circle:

    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return self.pi * (self. radius ** 2)
    def calculate_circumference(self):
        return 2 * self.pi * self.radius

circle_objekt = Circle(radius=5)

area = circle_objekt.calculate_area()
circumference = circle_objekt.calculate_circumference

print(f"area of the circle: {area}")
print(f"сircumference of a circle: {circumference}")

